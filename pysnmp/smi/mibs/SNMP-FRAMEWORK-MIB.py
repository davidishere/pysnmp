# PySNMP SMI module. Autogenerated from smidump -f python SNMP-FRAMEWORK-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 18:48:05 2006,
# Python version (2, 4, 3, 'final', 0)

try:
    import socket
except ImportError:
    pass
import string
import time

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class SnmpAdminString(TextualConvention, OctetString):
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)

class SnmpEngineID(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(5,32)
    try:
        # Attempt to base engine ID on local IP address
        defaultValue = '\x80\x00\x4f\xb8' + '\x01' + string.join(
            map(lambda x: chr(int(x)),
                string.split(socket.gethostbyname(socket.gethostname()),'.')),
            ''
            )
    except:
        # ...otherwise, use rudimentary text ID
        defaultValue = '\x80\x00\x4f\xb8' + '\x04' + 'mozhinka'

class SnmpEngineTime(Integer32):
    def clone(self, value=None, tagSet=None, subtypeSpec=None):
        # XXX
#        if value is None and self._value is not None:
#            value = int(time.time())-self._value
        return Integer32.clone(self, value, tagSet, subtypeSpec)
    
class SnmpMessageProcessingModel(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)

class SnmpSecurityLevel(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,3,2,)
    namedValues = namedval.NamedValues(("noAuthNoPriv", 1), ("authNoPriv", 2), ("authPriv", 3), )

class SnmpSecurityModel(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)

# Objects

snmpFrameworkMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 10)).setRevisions(("2002-10-14 00:00","1999-01-19 00:00","1997-11-20 00:00",))
snmpFrameworkAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1))
snmpAuthProtocols = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 1))
snmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 2))
snmpFrameworkMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 2))
snmpEngine = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 2, 1))
snmpEngineID = MibScalar((1, 3, 6, 1, 6, 3, 10, 2, 1, 1), SnmpEngineID()).setMaxAccess("readonly")
snmpEngineBoots = MibScalar((1, 3, 6, 1, 6, 3, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
snmpEngineTime = MibScalar((1, 3, 6, 1, 6, 3, 10, 2, 1, 3), SnmpEngineTime().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly").setUnits("seconds")
snmpEngineMaxMessageSize = MibScalar((1, 3, 6, 1, 6, 3, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(484, 2147483647L))).setMaxAccess("readonly")
snmpFrameworkMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 3))
snmpFrameworkMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 3, 1))
snmpFrameworkMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 3, 2))

# Augmentions

# Groups

snmpEngineGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 10, 3, 2, 1)).setObjects(("SNMP-FRAMEWORK-MIB", "snmpEngineID"), ("SNMP-FRAMEWORK-MIB", "snmpEngineBoots"), ("SNMP-FRAMEWORK-MIB", "snmpEngineMaxMessageSize"), ("SNMP-FRAMEWORK-MIB", "snmpEngineTime"), )

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-FRAMEWORK-MIB", PYSNMP_MODULE_ID=snmpFrameworkMIB)

# Types
mibBuilder.exportSymbols("SNMP-FRAMEWORK-MIB", SnmpAdminString=SnmpAdminString, SnmpEngineID=SnmpEngineID, SnmpMessageProcessingModel=SnmpMessageProcessingModel, SnmpSecurityLevel=SnmpSecurityLevel, SnmpSecurityModel=SnmpSecurityModel)

# Objects
mibBuilder.exportSymbols("SNMP-FRAMEWORK-MIB", snmpFrameworkMIB=snmpFrameworkMIB, snmpFrameworkAdmin=snmpFrameworkAdmin, snmpAuthProtocols=snmpAuthProtocols, snmpPrivProtocols=snmpPrivProtocols, snmpFrameworkMIBObjects=snmpFrameworkMIBObjects, snmpEngine=snmpEngine, snmpEngineID=snmpEngineID, snmpEngineBoots=snmpEngineBoots, snmpEngineTime=snmpEngineTime, snmpEngineMaxMessageSize=snmpEngineMaxMessageSize, snmpFrameworkMIBConformance=snmpFrameworkMIBConformance, snmpFrameworkMIBCompliances=snmpFrameworkMIBCompliances, snmpFrameworkMIBGroups=snmpFrameworkMIBGroups)

# Groups
mibBuilder.exportSymbols("SNMP-FRAMEWORK-MIB", snmpEngineGroup=snmpEngineGroup)
