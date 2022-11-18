
"""
    Copyright (c) 2022 Rahul Chaudhary Official (https://github.com/rahulchaudharyofficial) - All Rights Reserved.
    You are free to use, modify this code for personal or commercial use without any guarantee but do not remove copyright.
"""

from xml.dom.minidom import parseString

class MetadataConstantsProvider:
    def __init__(self) -> None:
        self.PACKAGE_START = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Package xmlns="http://soap.sforce.com/2006/04/self.metadata">\n'
        self.TYPES_START = '<types>'
        self.TYPES_END = '</types>'
        self.MEMBERS_START = '<members>'
        self.MEMBERS_END = '</members>'
        self.NAME_START = '<name>'
        self.NAME_END = '</name>'
        self.VERSION_START = '<version>'
        self.VERSION_END = '</version>'
        self.PACKAGE_END = '</Package>'
        self.NEW_LINE = '\n'
        self.VERSION_NUM = '55.0'
        self.CHAR_TAB = '\t'
        self.LOADING = '*loading..'
        self.infoMsg = 'All metadata selected except'
        self.ALL_ITEMS='*'
        self.METADATA_NAME = ['AccountRelationshipShareRule', 'ActionLinkGroupTemplate', 'ApexClass', 'ApexComponent',
                              'ApexPage', 'ApexTrigger', 'AppMenu', 'ApprovalProcess', 'ArticleType', 'AssignmentRules', 'Audience', 'AuthProvider',
                              'AuraDefinitionBundle', 'AutoResponseRules', 'Bot', 'BrandingSet', 'CallCenter', 'Certificate', 'CleanDataService',
                              'CMSConnectSource', 'Community', 'CommunityTemplateDefinition', 'CommunityThemeDefinition', 'CompactLayout',
                              'ConnectedApp', 'ContentAsset', 'CorsWhitelistOrigin', 'CustomApplication', 'CustomApplicationComponent',
                              'CustomFeedFilter', 'CustomHelpMenuSection', 'CustomMetadata', 'CustomLabels', 'CustomObjectTranslation',
                              'CustomPageWebLink', 'CustomPermission', 'CustomSite', 'CustomTab', 'DataCategoryGroup', 'DelegateGroup',
                              'DuplicateRule', 'EclairGeoData', 'EntitlementProcess', 'EntitlementTemplate', 'EventDelivery', 'EventSubscription',
                              'ExternalServiceRegistration', 'ExternalDataSource', 'FeatureParameterBoolean', 'FeatureParameterDate', 'FeatureParameterInteger',
                              'FieldSet', 'FlexiPage', 'Flow', 'FlowCategory', 'FlowDefinition', 'GlobalValueSet', 'GlobalValueSetTranslation', 'Group', 'HomePageComponent',
                              'HomePageLayout', 'InstalledPackage', 'KeywordList', 'Layout', 'LightningBolt', 'LightningComponentBundle', 'LightningExperienceTheme',
                              'LiveChatAgentConfig', 'LiveChatButton', 'LiveChatDeployment', 'LiveChatSensitiveDataRule', 'ManagedTopics', 'MatchingRules', 'MilestoneType',
                              'MlDomain', 'ModerationRule', 'NamedCredential', 'Network', 'NetworkBranding', 'PathAssistant', 'PermissionSet', 'PlatformCachePartition',
                              'Portal', 'PostTemplate', 'PresenceDeclineReason', 'PresenceUserConfig', 'Profile', 'ProfilePasswordPolicy', 'ProfileSessionSetting',
                              'Queue', 'QueueRoutingConfig', 'QuickAction', 'RecommendationStrategy', 'RecordActionDeployment', 'ReportType', 'Role', 'SamlSsoConfig',
                              'Scontrol', 'ServiceChannel', 'ServicePresenceStatus', 'SharingRules', 'SharingSet', 'SiteDotCom', 'Skill', 'StandardValueSetTranslation',
                              'StaticResource', 'SynonymDictionary', 'Territory', 'Territory2', 'Territory2Model', 'Territory2Rule', 'Territory2Type', 'TopicsForObjects',
                              'TransactionSecurityPolicy', 'Translations', 'WaveApplication', 'WaveDashboard', 'WaveDataflow', 'WaveDataset', 'WaveLens', 'WaveTemplateBundle',
                              'WaveXmd', 'Workflow','ActionPlanTemplate',
                              'AnimationRule',
                              'ChannelLayout',
                              'ApexTestSuite',
                              'AppointmentSchedulingPolicy',
                              'CampaignInfluenceModel',
                              'ChatterExtension',
                              'CspTrustedSite',
                              'CompactLayout',
                              'ExperienceBundle',
                              'LightningMessageChannel',
                              'MyDomainDiscoverableLogin',
                              'NavigationMenu',
                              'OauthCustomScope',
                              'PaymentGatewayProvider',
                              'PlatformEventChannel',
                              'PlatformEventChannelMember',
                              'Prompt',
                              'RedirectWhitelistUrl',
                              'Settings',
                              'TimeSheetTemplate',
                              'WaveRecipe',
                              'WorkSkillRouting']


def build_package(m: MetadataConstantsProvider) -> str:
    result:str = ''
    result += m.PACKAGE_START
    for meta_name in m.METADATA_NAME:
        result += m.TYPES_START #+'\n'
        result += m.MEMBERS_START+m.ALL_ITEMS+m.MEMBERS_END
        #result += '\n'
        result += m.NAME_START+meta_name+m.NAME_END
        #result += '\n'
        result += m.TYPES_END#+'\n'
    result += m.PACKAGE_END
    return result

def main() -> None:
    c = MetadataConstantsProvider()
    result = build_package(c)
    dom = parseString(result)
    with open("package.xml","w",encoding="utf-8") as f:
        f.write(dom.toprettyxml())


if __name__ == "__main__":
    main()
