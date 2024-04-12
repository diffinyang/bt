# coding: utf-8
##############################################################################
# Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

same70xultComponentIDList = ["usart0", "sys_time", "tc0"]		
same70xultAutoConnectList = [["bluetooth_bm64", "USART PLIB", "usart0", "USART0_UART"],
                          ["sys_time", "sys_time_TMR_dependency", "tc0", "TC0_TMR"]]
same70xultPinConfigs = [{"pin": 20, "name": "USART0_TXD0", "type": "USART0_TXD0", "direction": "", "latch": "", "abcd": "C"},  # PB1
                     {"pin": 21, "name": "USART0_RXD0", "type": "USART0_RXD0", "direction": "", "latch": "", "abcd": "C"},  # PB0
                     {"pin": 26, "name": "BM64_MFB", "type": "GPIO", "direction": "Out", "latch": "Low", "abcd": ""},       # PB2
                     {"pin": 98, "name": "STBYRST", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}]       # PD11 

sam_e70_xplained_ultra = bspSupportObj(same70xultPinConfigs, same70xultComponentIDList, None, same70xultAutoConnectList, None)					

addBSPSupport("BSP_SAM_E70_Xplained_Ultra", "E70_XPLAINED_ULTRA", sam_e70_xplained_ultra)