import  unittest

from    osbot_aws.apis.Lambda import Lambda
from    pbx_gs_python_utils.utils.Dev         import Dev

from osbot_jira.api.GS_Bot_Jira import GS_Bot_Jira
from osbot_jira.lambdas.elastic_jira import run

class test_lambda_elastic_jira(unittest.TestCase):
    def setUp(self):
        self.jira_issues = Lambda('osbot_jira.lambdas.elastic_jira')

        #from osbot_jira.Deploy import Deploy
        #Deploy('osbot_jira.lambdas.elastic_jira').deploy()

    def test_invoke_directly(self):
        response = run({},{})
        assert response == { 'attachments': [],
                             'text': ':point_right: no command received, see `jira help` for a list of '
                                      'available commands`'}

    def test_invoke_directly__version(self):
        response = run({'params':['version']},{})
        assert response == GS_Bot_Jira().version


    def test_update_invoke(self):
        key = 'RISK-424'
        issue = self.jira_issues.invoke({"params": ['issue', key], "channel": 'GDL2EC3EE'})
        assert issue.get('text') == '....._fetching data for *<https://jira.photobox.com/browse/RISK-424|RISK-424>* _from index:_ *jira*'

    def test_update_invoke__link_links(self):
        id = 'RISK-1'
        assert self.jira_issues.invoke({"params": ["issue-links", id], "channel": 'GDL2EC3EE'}).get('text') == ':red_circle: Not supported command `issue-links` , see all available using `jira help`'

    # def test_update_invoke__link_share(self):
    #     id = 'RISK-2'
    #     #issue = self.jira_issues.update_with_src().invoke({"params": ["issue", id], "channel": 'GDL2EC3EE'})
    #     #issue = self.jira_issues.update_with_src().invoke({"params": ["issue-links", id], "channel": 'GDL2EC3EE'})
    #     result = self.jira_issues.invoke({"params": [ 'link_shared', '[{"url":"https://jira.photobox.com/browse/SEC-1234"}]'], "channel": 'GDL2EC3EE'})
    #
    #     #Dev.pprint(result)


    def test_invoke_bad_cmd(self):
        result = self.jira_issues.invoke({"params": ["aaaa"], 'user' : 'abc'})
        assert result == { 'attachments': [],
                          'text': ':red_circle: Not supported command `aaaa` , see all available using `jira help`'}

    def test_invoke_version(self):
        assert self.jira_issues.invoke({"params": ["version"]}) == GS_Bot_Jira().version

        #assert self.jira_issues.invoke({"params": ["version"]}).get('text') == '123'


    # BUG issue doesn't return data
    # def test_invoke__no_data_for_issue(self):
    #     issue_id = 'GSCS-24'
    #     result = self.jira_issues.invoke({"params": ['issue',issue_id], 'team_id':'T7F3AUXGV', 'channel':'GDL2EC3EE' })
    #     Dev.pprint(result)