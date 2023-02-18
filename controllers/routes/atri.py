import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"Flex2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex9":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div6":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div7":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex18":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex20":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div14":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div13":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex25":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div15":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex29":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div19":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex26":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex27":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex28":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div16":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex36":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div39":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div41":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div42":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex38":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div31":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div32":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div33":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div34":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex41":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div35":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div36":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div37":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div38":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex44":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div44":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex45":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div45":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex46":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex47":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div46":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div47":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex48":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div49":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div50":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex49":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div51":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div55":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex50":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div56":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div57":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div73":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div76":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div80":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div81":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"TextBox46":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox50":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox51":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div85":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div86":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Image2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox17":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button11":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox19":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button12":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox20":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox25":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Button13":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button14":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox36":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox33":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox34":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox35":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image9":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image12":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox43":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image13":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox44":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image14":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox45":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox37":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox38":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button15":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button16":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Image36":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox102":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox103":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button21":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button22":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox75":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox76":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image28":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox77":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox78":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox79":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image29":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox80":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox81":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox82":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image30":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox83":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox84":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox85":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image31":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox86":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox87":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image32":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox88":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox89":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox90":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image33":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox91":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox92":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox93":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image34":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox94":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox95":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox96":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image35":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox97":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox98":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button18":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button19":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox104":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox105":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image37":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image38":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox106":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox107":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image43":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image44":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image46":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image47":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image48":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image49":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image45":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox109":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox110":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button23":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button24":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox114":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox115":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox116":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image53":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image54":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox118":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox119":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox126":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox127":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image58":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox128":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox129":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image59":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox130":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox131":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image60":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Div79":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"TextBox176":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox177":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.Flex2 = state["Flex2"]
		self.Flex9 = state["Flex9"]
		self.Div6 = state["Div6"]
		self.Div7 = state["Div7"]
		self.Flex18 = state["Flex18"]
		self.Flex20 = state["Flex20"]
		self.Div14 = state["Div14"]
		self.Div13 = state["Div13"]
		self.Flex25 = state["Flex25"]
		self.Div15 = state["Div15"]
		self.Flex29 = state["Flex29"]
		self.Div19 = state["Div19"]
		self.Flex26 = state["Flex26"]
		self.Flex27 = state["Flex27"]
		self.Flex28 = state["Flex28"]
		self.Div16 = state["Div16"]
		self.Flex36 = state["Flex36"]
		self.Div39 = state["Div39"]
		self.Div41 = state["Div41"]
		self.Div42 = state["Div42"]
		self.Flex38 = state["Flex38"]
		self.Div31 = state["Div31"]
		self.Div32 = state["Div32"]
		self.Div33 = state["Div33"]
		self.Div34 = state["Div34"]
		self.Flex41 = state["Flex41"]
		self.Div35 = state["Div35"]
		self.Div36 = state["Div36"]
		self.Div37 = state["Div37"]
		self.Div38 = state["Div38"]
		self.Flex44 = state["Flex44"]
		self.Div44 = state["Div44"]
		self.Flex45 = state["Flex45"]
		self.Div45 = state["Div45"]
		self.Flex46 = state["Flex46"]
		self.Flex47 = state["Flex47"]
		self.Div46 = state["Div46"]
		self.Div47 = state["Div47"]
		self.Flex48 = state["Flex48"]
		self.Div49 = state["Div49"]
		self.Div50 = state["Div50"]
		self.Flex49 = state["Flex49"]
		self.Div51 = state["Div51"]
		self.Div55 = state["Div55"]
		self.Flex50 = state["Flex50"]
		self.Div56 = state["Div56"]
		self.Div57 = state["Div57"]
		self.Div73 = state["Div73"]
		self.Div76 = state["Div76"]
		self.Div80 = state["Div80"]
		self.Div81 = state["Div81"]
		self.TextBox46 = state["TextBox46"]
		self.TextBox50 = state["TextBox50"]
		self.TextBox51 = state["TextBox51"]
		self.Div85 = state["Div85"]
		self.Div86 = state["Div86"]
		self.Image2 = state["Image2"]
		self.TextBox4 = state["TextBox4"]
		self.TextBox5 = state["TextBox5"]
		self.TextBox6 = state["TextBox6"]
		self.TextBox7 = state["TextBox7"]
		self.TextBox8 = state["TextBox8"]
		self.Button1 = state["Button1"]
		self.Button2 = state["Button2"]
		self.TextBox17 = state["TextBox17"]
		self.Button11 = state["Button11"]
		self.TextBox19 = state["TextBox19"]
		self.Button12 = state["Button12"]
		self.TextBox20 = state["TextBox20"]
		self.Image3 = state["Image3"]
		self.TextBox25 = state["TextBox25"]
		self.Image4 = state["Image4"]
		self.Image5 = state["Image5"]
		self.Image6 = state["Image6"]
		self.Image7 = state["Image7"]
		self.Button13 = state["Button13"]
		self.Button14 = state["Button14"]
		self.TextBox36 = state["TextBox36"]
		self.Image8 = state["Image8"]
		self.TextBox33 = state["TextBox33"]
		self.TextBox34 = state["TextBox34"]
		self.TextBox35 = state["TextBox35"]
		self.Image9 = state["Image9"]
		self.Image12 = state["Image12"]
		self.TextBox43 = state["TextBox43"]
		self.Image13 = state["Image13"]
		self.TextBox44 = state["TextBox44"]
		self.Image14 = state["Image14"]
		self.TextBox45 = state["TextBox45"]
		self.TextBox37 = state["TextBox37"]
		self.TextBox38 = state["TextBox38"]
		self.Button15 = state["Button15"]
		self.Button16 = state["Button16"]
		self.Image36 = state["Image36"]
		self.TextBox102 = state["TextBox102"]
		self.TextBox103 = state["TextBox103"]
		self.Button21 = state["Button21"]
		self.Button22 = state["Button22"]
		self.TextBox75 = state["TextBox75"]
		self.TextBox76 = state["TextBox76"]
		self.Image28 = state["Image28"]
		self.TextBox77 = state["TextBox77"]
		self.TextBox78 = state["TextBox78"]
		self.TextBox79 = state["TextBox79"]
		self.Image29 = state["Image29"]
		self.TextBox80 = state["TextBox80"]
		self.TextBox81 = state["TextBox81"]
		self.TextBox82 = state["TextBox82"]
		self.Image30 = state["Image30"]
		self.TextBox83 = state["TextBox83"]
		self.TextBox84 = state["TextBox84"]
		self.TextBox85 = state["TextBox85"]
		self.Image31 = state["Image31"]
		self.TextBox86 = state["TextBox86"]
		self.TextBox87 = state["TextBox87"]
		self.Image32 = state["Image32"]
		self.TextBox88 = state["TextBox88"]
		self.TextBox89 = state["TextBox89"]
		self.TextBox90 = state["TextBox90"]
		self.Image33 = state["Image33"]
		self.TextBox91 = state["TextBox91"]
		self.TextBox92 = state["TextBox92"]
		self.TextBox93 = state["TextBox93"]
		self.Image34 = state["Image34"]
		self.TextBox94 = state["TextBox94"]
		self.TextBox95 = state["TextBox95"]
		self.TextBox96 = state["TextBox96"]
		self.Image35 = state["Image35"]
		self.TextBox97 = state["TextBox97"]
		self.TextBox98 = state["TextBox98"]
		self.Button18 = state["Button18"]
		self.Button19 = state["Button19"]
		self.TextBox104 = state["TextBox104"]
		self.TextBox105 = state["TextBox105"]
		self.Image37 = state["Image37"]
		self.Image38 = state["Image38"]
		self.TextBox106 = state["TextBox106"]
		self.TextBox107 = state["TextBox107"]
		self.Image43 = state["Image43"]
		self.Image44 = state["Image44"]
		self.Image46 = state["Image46"]
		self.Image47 = state["Image47"]
		self.Image48 = state["Image48"]
		self.Image49 = state["Image49"]
		self.Image45 = state["Image45"]
		self.TextBox109 = state["TextBox109"]
		self.TextBox110 = state["TextBox110"]
		self.Button23 = state["Button23"]
		self.Button24 = state["Button24"]
		self.TextBox114 = state["TextBox114"]
		self.TextBox115 = state["TextBox115"]
		self.TextBox116 = state["TextBox116"]
		self.Image53 = state["Image53"]
		self.Image54 = state["Image54"]
		self.TextBox118 = state["TextBox118"]
		self.TextBox119 = state["TextBox119"]
		self.TextBox126 = state["TextBox126"]
		self.TextBox127 = state["TextBox127"]
		self.Image58 = state["Image58"]
		self.TextBox128 = state["TextBox128"]
		self.TextBox129 = state["TextBox129"]
		self.Image59 = state["Image59"]
		self.TextBox130 = state["TextBox130"]
		self.TextBox131 = state["TextBox131"]
		self.Image60 = state["Image60"]
		self.Div79 = state["Div79"]
		self.TextBox176 = state["TextBox176"]
		self.TextBox177 = state["TextBox177"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		global default_state
		self._Flex2 = Flex(new_state, default_state["Flex2"])

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		global default_state
		self._Flex9 = Flex(new_state, default_state["Flex9"])

	@property
	def Div6(self):
		self._getter_access_tracker["Div6"] = {}
		return self._Div6
	@Div6.setter
	def Div6(self, new_state):
		self._setter_access_tracker["Div6"] = {}
		global default_state
		self._Div6 = Div(new_state, default_state["Div6"])

	@property
	def Div7(self):
		self._getter_access_tracker["Div7"] = {}
		return self._Div7
	@Div7.setter
	def Div7(self, new_state):
		self._setter_access_tracker["Div7"] = {}
		global default_state
		self._Div7 = Div(new_state, default_state["Div7"])

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		global default_state
		self._Flex18 = Flex(new_state, default_state["Flex18"])

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		global default_state
		self._Flex20 = Flex(new_state, default_state["Flex20"])

	@property
	def Div14(self):
		self._getter_access_tracker["Div14"] = {}
		return self._Div14
	@Div14.setter
	def Div14(self, new_state):
		self._setter_access_tracker["Div14"] = {}
		global default_state
		self._Div14 = Div(new_state, default_state["Div14"])

	@property
	def Div13(self):
		self._getter_access_tracker["Div13"] = {}
		return self._Div13
	@Div13.setter
	def Div13(self, new_state):
		self._setter_access_tracker["Div13"] = {}
		global default_state
		self._Div13 = Div(new_state, default_state["Div13"])

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		global default_state
		self._Flex25 = Flex(new_state, default_state["Flex25"])

	@property
	def Div15(self):
		self._getter_access_tracker["Div15"] = {}
		return self._Div15
	@Div15.setter
	def Div15(self, new_state):
		self._setter_access_tracker["Div15"] = {}
		global default_state
		self._Div15 = Div(new_state, default_state["Div15"])

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		global default_state
		self._Flex29 = Flex(new_state, default_state["Flex29"])

	@property
	def Div19(self):
		self._getter_access_tracker["Div19"] = {}
		return self._Div19
	@Div19.setter
	def Div19(self, new_state):
		self._setter_access_tracker["Div19"] = {}
		global default_state
		self._Div19 = Div(new_state, default_state["Div19"])

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		global default_state
		self._Flex26 = Flex(new_state, default_state["Flex26"])

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		global default_state
		self._Flex27 = Flex(new_state, default_state["Flex27"])

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		global default_state
		self._Flex28 = Flex(new_state, default_state["Flex28"])

	@property
	def Div16(self):
		self._getter_access_tracker["Div16"] = {}
		return self._Div16
	@Div16.setter
	def Div16(self, new_state):
		self._setter_access_tracker["Div16"] = {}
		global default_state
		self._Div16 = Div(new_state, default_state["Div16"])

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		global default_state
		self._Flex36 = Flex(new_state, default_state["Flex36"])

	@property
	def Div39(self):
		self._getter_access_tracker["Div39"] = {}
		return self._Div39
	@Div39.setter
	def Div39(self, new_state):
		self._setter_access_tracker["Div39"] = {}
		global default_state
		self._Div39 = Div(new_state, default_state["Div39"])

	@property
	def Div41(self):
		self._getter_access_tracker["Div41"] = {}
		return self._Div41
	@Div41.setter
	def Div41(self, new_state):
		self._setter_access_tracker["Div41"] = {}
		global default_state
		self._Div41 = Div(new_state, default_state["Div41"])

	@property
	def Div42(self):
		self._getter_access_tracker["Div42"] = {}
		return self._Div42
	@Div42.setter
	def Div42(self, new_state):
		self._setter_access_tracker["Div42"] = {}
		global default_state
		self._Div42 = Div(new_state, default_state["Div42"])

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		global default_state
		self._Flex38 = Flex(new_state, default_state["Flex38"])

	@property
	def Div31(self):
		self._getter_access_tracker["Div31"] = {}
		return self._Div31
	@Div31.setter
	def Div31(self, new_state):
		self._setter_access_tracker["Div31"] = {}
		global default_state
		self._Div31 = Div(new_state, default_state["Div31"])

	@property
	def Div32(self):
		self._getter_access_tracker["Div32"] = {}
		return self._Div32
	@Div32.setter
	def Div32(self, new_state):
		self._setter_access_tracker["Div32"] = {}
		global default_state
		self._Div32 = Div(new_state, default_state["Div32"])

	@property
	def Div33(self):
		self._getter_access_tracker["Div33"] = {}
		return self._Div33
	@Div33.setter
	def Div33(self, new_state):
		self._setter_access_tracker["Div33"] = {}
		global default_state
		self._Div33 = Div(new_state, default_state["Div33"])

	@property
	def Div34(self):
		self._getter_access_tracker["Div34"] = {}
		return self._Div34
	@Div34.setter
	def Div34(self, new_state):
		self._setter_access_tracker["Div34"] = {}
		global default_state
		self._Div34 = Div(new_state, default_state["Div34"])

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		global default_state
		self._Flex41 = Flex(new_state, default_state["Flex41"])

	@property
	def Div35(self):
		self._getter_access_tracker["Div35"] = {}
		return self._Div35
	@Div35.setter
	def Div35(self, new_state):
		self._setter_access_tracker["Div35"] = {}
		global default_state
		self._Div35 = Div(new_state, default_state["Div35"])

	@property
	def Div36(self):
		self._getter_access_tracker["Div36"] = {}
		return self._Div36
	@Div36.setter
	def Div36(self, new_state):
		self._setter_access_tracker["Div36"] = {}
		global default_state
		self._Div36 = Div(new_state, default_state["Div36"])

	@property
	def Div37(self):
		self._getter_access_tracker["Div37"] = {}
		return self._Div37
	@Div37.setter
	def Div37(self, new_state):
		self._setter_access_tracker["Div37"] = {}
		global default_state
		self._Div37 = Div(new_state, default_state["Div37"])

	@property
	def Div38(self):
		self._getter_access_tracker["Div38"] = {}
		return self._Div38
	@Div38.setter
	def Div38(self, new_state):
		self._setter_access_tracker["Div38"] = {}
		global default_state
		self._Div38 = Div(new_state, default_state["Div38"])

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		global default_state
		self._Flex44 = Flex(new_state, default_state["Flex44"])

	@property
	def Div44(self):
		self._getter_access_tracker["Div44"] = {}
		return self._Div44
	@Div44.setter
	def Div44(self, new_state):
		self._setter_access_tracker["Div44"] = {}
		global default_state
		self._Div44 = Div(new_state, default_state["Div44"])

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		global default_state
		self._Flex45 = Flex(new_state, default_state["Flex45"])

	@property
	def Div45(self):
		self._getter_access_tracker["Div45"] = {}
		return self._Div45
	@Div45.setter
	def Div45(self, new_state):
		self._setter_access_tracker["Div45"] = {}
		global default_state
		self._Div45 = Div(new_state, default_state["Div45"])

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		global default_state
		self._Flex46 = Flex(new_state, default_state["Flex46"])

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		global default_state
		self._Flex47 = Flex(new_state, default_state["Flex47"])

	@property
	def Div46(self):
		self._getter_access_tracker["Div46"] = {}
		return self._Div46
	@Div46.setter
	def Div46(self, new_state):
		self._setter_access_tracker["Div46"] = {}
		global default_state
		self._Div46 = Div(new_state, default_state["Div46"])

	@property
	def Div47(self):
		self._getter_access_tracker["Div47"] = {}
		return self._Div47
	@Div47.setter
	def Div47(self, new_state):
		self._setter_access_tracker["Div47"] = {}
		global default_state
		self._Div47 = Div(new_state, default_state["Div47"])

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		global default_state
		self._Flex48 = Flex(new_state, default_state["Flex48"])

	@property
	def Div49(self):
		self._getter_access_tracker["Div49"] = {}
		return self._Div49
	@Div49.setter
	def Div49(self, new_state):
		self._setter_access_tracker["Div49"] = {}
		global default_state
		self._Div49 = Div(new_state, default_state["Div49"])

	@property
	def Div50(self):
		self._getter_access_tracker["Div50"] = {}
		return self._Div50
	@Div50.setter
	def Div50(self, new_state):
		self._setter_access_tracker["Div50"] = {}
		global default_state
		self._Div50 = Div(new_state, default_state["Div50"])

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		global default_state
		self._Flex49 = Flex(new_state, default_state["Flex49"])

	@property
	def Div51(self):
		self._getter_access_tracker["Div51"] = {}
		return self._Div51
	@Div51.setter
	def Div51(self, new_state):
		self._setter_access_tracker["Div51"] = {}
		global default_state
		self._Div51 = Div(new_state, default_state["Div51"])

	@property
	def Div55(self):
		self._getter_access_tracker["Div55"] = {}
		return self._Div55
	@Div55.setter
	def Div55(self, new_state):
		self._setter_access_tracker["Div55"] = {}
		global default_state
		self._Div55 = Div(new_state, default_state["Div55"])

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		global default_state
		self._Flex50 = Flex(new_state, default_state["Flex50"])

	@property
	def Div56(self):
		self._getter_access_tracker["Div56"] = {}
		return self._Div56
	@Div56.setter
	def Div56(self, new_state):
		self._setter_access_tracker["Div56"] = {}
		global default_state
		self._Div56 = Div(new_state, default_state["Div56"])

	@property
	def Div57(self):
		self._getter_access_tracker["Div57"] = {}
		return self._Div57
	@Div57.setter
	def Div57(self, new_state):
		self._setter_access_tracker["Div57"] = {}
		global default_state
		self._Div57 = Div(new_state, default_state["Div57"])

	@property
	def Div73(self):
		self._getter_access_tracker["Div73"] = {}
		return self._Div73
	@Div73.setter
	def Div73(self, new_state):
		self._setter_access_tracker["Div73"] = {}
		global default_state
		self._Div73 = Div(new_state, default_state["Div73"])

	@property
	def Div76(self):
		self._getter_access_tracker["Div76"] = {}
		return self._Div76
	@Div76.setter
	def Div76(self, new_state):
		self._setter_access_tracker["Div76"] = {}
		global default_state
		self._Div76 = Div(new_state, default_state["Div76"])

	@property
	def Div80(self):
		self._getter_access_tracker["Div80"] = {}
		return self._Div80
	@Div80.setter
	def Div80(self, new_state):
		self._setter_access_tracker["Div80"] = {}
		global default_state
		self._Div80 = Div(new_state, default_state["Div80"])

	@property
	def Div81(self):
		self._getter_access_tracker["Div81"] = {}
		return self._Div81
	@Div81.setter
	def Div81(self, new_state):
		self._setter_access_tracker["Div81"] = {}
		global default_state
		self._Div81 = Div(new_state, default_state["Div81"])

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		global default_state
		self._TextBox46 = TextBox(new_state, default_state["TextBox46"])

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		global default_state
		self._TextBox50 = TextBox(new_state, default_state["TextBox50"])

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		global default_state
		self._TextBox51 = TextBox(new_state, default_state["TextBox51"])

	@property
	def Div85(self):
		self._getter_access_tracker["Div85"] = {}
		return self._Div85
	@Div85.setter
	def Div85(self, new_state):
		self._setter_access_tracker["Div85"] = {}
		global default_state
		self._Div85 = Div(new_state, default_state["Div85"])

	@property
	def Div86(self):
		self._getter_access_tracker["Div86"] = {}
		return self._Div86
	@Div86.setter
	def Div86(self, new_state):
		self._setter_access_tracker["Div86"] = {}
		global default_state
		self._Div86 = Div(new_state, default_state["Div86"])

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		global default_state
		self._Image2 = Image(new_state, default_state["Image2"])

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		global default_state
		self._TextBox4 = TextBox(new_state, default_state["TextBox4"])

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		global default_state
		self._TextBox5 = TextBox(new_state, default_state["TextBox5"])

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		global default_state
		self._TextBox6 = TextBox(new_state, default_state["TextBox6"])

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		global default_state
		self._TextBox7 = TextBox(new_state, default_state["TextBox7"])

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		global default_state
		self._TextBox8 = TextBox(new_state, default_state["TextBox8"])

	@property
	def Button1(self):
		self._getter_access_tracker["Button1"] = {}
		return self._Button1
	@Button1.setter
	def Button1(self, new_state):
		self._setter_access_tracker["Button1"] = {}
		global default_state
		self._Button1 = Button(new_state, default_state["Button1"])

	@property
	def Button2(self):
		self._getter_access_tracker["Button2"] = {}
		return self._Button2
	@Button2.setter
	def Button2(self, new_state):
		self._setter_access_tracker["Button2"] = {}
		global default_state
		self._Button2 = Button(new_state, default_state["Button2"])

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		global default_state
		self._TextBox17 = TextBox(new_state, default_state["TextBox17"])

	@property
	def Button11(self):
		self._getter_access_tracker["Button11"] = {}
		return self._Button11
	@Button11.setter
	def Button11(self, new_state):
		self._setter_access_tracker["Button11"] = {}
		global default_state
		self._Button11 = Button(new_state, default_state["Button11"])

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		global default_state
		self._TextBox19 = TextBox(new_state, default_state["TextBox19"])

	@property
	def Button12(self):
		self._getter_access_tracker["Button12"] = {}
		return self._Button12
	@Button12.setter
	def Button12(self, new_state):
		self._setter_access_tracker["Button12"] = {}
		global default_state
		self._Button12 = Button(new_state, default_state["Button12"])

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		global default_state
		self._TextBox20 = TextBox(new_state, default_state["TextBox20"])

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		global default_state
		self._Image3 = Image(new_state, default_state["Image3"])

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		global default_state
		self._TextBox25 = TextBox(new_state, default_state["TextBox25"])

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		global default_state
		self._Image4 = Image(new_state, default_state["Image4"])

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		global default_state
		self._Image5 = Image(new_state, default_state["Image5"])

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		global default_state
		self._Image6 = Image(new_state, default_state["Image6"])

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		global default_state
		self._Image7 = Image(new_state, default_state["Image7"])

	@property
	def Button13(self):
		self._getter_access_tracker["Button13"] = {}
		return self._Button13
	@Button13.setter
	def Button13(self, new_state):
		self._setter_access_tracker["Button13"] = {}
		global default_state
		self._Button13 = Button(new_state, default_state["Button13"])

	@property
	def Button14(self):
		self._getter_access_tracker["Button14"] = {}
		return self._Button14
	@Button14.setter
	def Button14(self, new_state):
		self._setter_access_tracker["Button14"] = {}
		global default_state
		self._Button14 = Button(new_state, default_state["Button14"])

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		global default_state
		self._TextBox36 = TextBox(new_state, default_state["TextBox36"])

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		global default_state
		self._Image8 = Image(new_state, default_state["Image8"])

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		global default_state
		self._TextBox33 = TextBox(new_state, default_state["TextBox33"])

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		global default_state
		self._TextBox34 = TextBox(new_state, default_state["TextBox34"])

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		global default_state
		self._TextBox35 = TextBox(new_state, default_state["TextBox35"])

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		global default_state
		self._Image9 = Image(new_state, default_state["Image9"])

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		global default_state
		self._Image12 = Image(new_state, default_state["Image12"])

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		global default_state
		self._TextBox43 = TextBox(new_state, default_state["TextBox43"])

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		global default_state
		self._Image13 = Image(new_state, default_state["Image13"])

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		global default_state
		self._TextBox44 = TextBox(new_state, default_state["TextBox44"])

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		global default_state
		self._Image14 = Image(new_state, default_state["Image14"])

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		global default_state
		self._TextBox45 = TextBox(new_state, default_state["TextBox45"])

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		global default_state
		self._TextBox37 = TextBox(new_state, default_state["TextBox37"])

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		global default_state
		self._TextBox38 = TextBox(new_state, default_state["TextBox38"])

	@property
	def Button15(self):
		self._getter_access_tracker["Button15"] = {}
		return self._Button15
	@Button15.setter
	def Button15(self, new_state):
		self._setter_access_tracker["Button15"] = {}
		global default_state
		self._Button15 = Button(new_state, default_state["Button15"])

	@property
	def Button16(self):
		self._getter_access_tracker["Button16"] = {}
		return self._Button16
	@Button16.setter
	def Button16(self, new_state):
		self._setter_access_tracker["Button16"] = {}
		global default_state
		self._Button16 = Button(new_state, default_state["Button16"])

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		global default_state
		self._Image36 = Image(new_state, default_state["Image36"])

	@property
	def TextBox102(self):
		self._getter_access_tracker["TextBox102"] = {}
		return self._TextBox102
	@TextBox102.setter
	def TextBox102(self, new_state):
		self._setter_access_tracker["TextBox102"] = {}
		global default_state
		self._TextBox102 = TextBox(new_state, default_state["TextBox102"])

	@property
	def TextBox103(self):
		self._getter_access_tracker["TextBox103"] = {}
		return self._TextBox103
	@TextBox103.setter
	def TextBox103(self, new_state):
		self._setter_access_tracker["TextBox103"] = {}
		global default_state
		self._TextBox103 = TextBox(new_state, default_state["TextBox103"])

	@property
	def Button21(self):
		self._getter_access_tracker["Button21"] = {}
		return self._Button21
	@Button21.setter
	def Button21(self, new_state):
		self._setter_access_tracker["Button21"] = {}
		global default_state
		self._Button21 = Button(new_state, default_state["Button21"])

	@property
	def Button22(self):
		self._getter_access_tracker["Button22"] = {}
		return self._Button22
	@Button22.setter
	def Button22(self, new_state):
		self._setter_access_tracker["Button22"] = {}
		global default_state
		self._Button22 = Button(new_state, default_state["Button22"])

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		global default_state
		self._TextBox75 = TextBox(new_state, default_state["TextBox75"])

	@property
	def TextBox76(self):
		self._getter_access_tracker["TextBox76"] = {}
		return self._TextBox76
	@TextBox76.setter
	def TextBox76(self, new_state):
		self._setter_access_tracker["TextBox76"] = {}
		global default_state
		self._TextBox76 = TextBox(new_state, default_state["TextBox76"])

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		global default_state
		self._Image28 = Image(new_state, default_state["Image28"])

	@property
	def TextBox77(self):
		self._getter_access_tracker["TextBox77"] = {}
		return self._TextBox77
	@TextBox77.setter
	def TextBox77(self, new_state):
		self._setter_access_tracker["TextBox77"] = {}
		global default_state
		self._TextBox77 = TextBox(new_state, default_state["TextBox77"])

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		global default_state
		self._TextBox78 = TextBox(new_state, default_state["TextBox78"])

	@property
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		global default_state
		self._TextBox79 = TextBox(new_state, default_state["TextBox79"])

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		global default_state
		self._Image29 = Image(new_state, default_state["Image29"])

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		global default_state
		self._TextBox80 = TextBox(new_state, default_state["TextBox80"])

	@property
	def TextBox81(self):
		self._getter_access_tracker["TextBox81"] = {}
		return self._TextBox81
	@TextBox81.setter
	def TextBox81(self, new_state):
		self._setter_access_tracker["TextBox81"] = {}
		global default_state
		self._TextBox81 = TextBox(new_state, default_state["TextBox81"])

	@property
	def TextBox82(self):
		self._getter_access_tracker["TextBox82"] = {}
		return self._TextBox82
	@TextBox82.setter
	def TextBox82(self, new_state):
		self._setter_access_tracker["TextBox82"] = {}
		global default_state
		self._TextBox82 = TextBox(new_state, default_state["TextBox82"])

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		global default_state
		self._Image30 = Image(new_state, default_state["Image30"])

	@property
	def TextBox83(self):
		self._getter_access_tracker["TextBox83"] = {}
		return self._TextBox83
	@TextBox83.setter
	def TextBox83(self, new_state):
		self._setter_access_tracker["TextBox83"] = {}
		global default_state
		self._TextBox83 = TextBox(new_state, default_state["TextBox83"])

	@property
	def TextBox84(self):
		self._getter_access_tracker["TextBox84"] = {}
		return self._TextBox84
	@TextBox84.setter
	def TextBox84(self, new_state):
		self._setter_access_tracker["TextBox84"] = {}
		global default_state
		self._TextBox84 = TextBox(new_state, default_state["TextBox84"])

	@property
	def TextBox85(self):
		self._getter_access_tracker["TextBox85"] = {}
		return self._TextBox85
	@TextBox85.setter
	def TextBox85(self, new_state):
		self._setter_access_tracker["TextBox85"] = {}
		global default_state
		self._TextBox85 = TextBox(new_state, default_state["TextBox85"])

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		global default_state
		self._Image31 = Image(new_state, default_state["Image31"])

	@property
	def TextBox86(self):
		self._getter_access_tracker["TextBox86"] = {}
		return self._TextBox86
	@TextBox86.setter
	def TextBox86(self, new_state):
		self._setter_access_tracker["TextBox86"] = {}
		global default_state
		self._TextBox86 = TextBox(new_state, default_state["TextBox86"])

	@property
	def TextBox87(self):
		self._getter_access_tracker["TextBox87"] = {}
		return self._TextBox87
	@TextBox87.setter
	def TextBox87(self, new_state):
		self._setter_access_tracker["TextBox87"] = {}
		global default_state
		self._TextBox87 = TextBox(new_state, default_state["TextBox87"])

	@property
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		global default_state
		self._Image32 = Image(new_state, default_state["Image32"])

	@property
	def TextBox88(self):
		self._getter_access_tracker["TextBox88"] = {}
		return self._TextBox88
	@TextBox88.setter
	def TextBox88(self, new_state):
		self._setter_access_tracker["TextBox88"] = {}
		global default_state
		self._TextBox88 = TextBox(new_state, default_state["TextBox88"])

	@property
	def TextBox89(self):
		self._getter_access_tracker["TextBox89"] = {}
		return self._TextBox89
	@TextBox89.setter
	def TextBox89(self, new_state):
		self._setter_access_tracker["TextBox89"] = {}
		global default_state
		self._TextBox89 = TextBox(new_state, default_state["TextBox89"])

	@property
	def TextBox90(self):
		self._getter_access_tracker["TextBox90"] = {}
		return self._TextBox90
	@TextBox90.setter
	def TextBox90(self, new_state):
		self._setter_access_tracker["TextBox90"] = {}
		global default_state
		self._TextBox90 = TextBox(new_state, default_state["TextBox90"])

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		global default_state
		self._Image33 = Image(new_state, default_state["Image33"])

	@property
	def TextBox91(self):
		self._getter_access_tracker["TextBox91"] = {}
		return self._TextBox91
	@TextBox91.setter
	def TextBox91(self, new_state):
		self._setter_access_tracker["TextBox91"] = {}
		global default_state
		self._TextBox91 = TextBox(new_state, default_state["TextBox91"])

	@property
	def TextBox92(self):
		self._getter_access_tracker["TextBox92"] = {}
		return self._TextBox92
	@TextBox92.setter
	def TextBox92(self, new_state):
		self._setter_access_tracker["TextBox92"] = {}
		global default_state
		self._TextBox92 = TextBox(new_state, default_state["TextBox92"])

	@property
	def TextBox93(self):
		self._getter_access_tracker["TextBox93"] = {}
		return self._TextBox93
	@TextBox93.setter
	def TextBox93(self, new_state):
		self._setter_access_tracker["TextBox93"] = {}
		global default_state
		self._TextBox93 = TextBox(new_state, default_state["TextBox93"])

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		global default_state
		self._Image34 = Image(new_state, default_state["Image34"])

	@property
	def TextBox94(self):
		self._getter_access_tracker["TextBox94"] = {}
		return self._TextBox94
	@TextBox94.setter
	def TextBox94(self, new_state):
		self._setter_access_tracker["TextBox94"] = {}
		global default_state
		self._TextBox94 = TextBox(new_state, default_state["TextBox94"])

	@property
	def TextBox95(self):
		self._getter_access_tracker["TextBox95"] = {}
		return self._TextBox95
	@TextBox95.setter
	def TextBox95(self, new_state):
		self._setter_access_tracker["TextBox95"] = {}
		global default_state
		self._TextBox95 = TextBox(new_state, default_state["TextBox95"])

	@property
	def TextBox96(self):
		self._getter_access_tracker["TextBox96"] = {}
		return self._TextBox96
	@TextBox96.setter
	def TextBox96(self, new_state):
		self._setter_access_tracker["TextBox96"] = {}
		global default_state
		self._TextBox96 = TextBox(new_state, default_state["TextBox96"])

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		global default_state
		self._Image35 = Image(new_state, default_state["Image35"])

	@property
	def TextBox97(self):
		self._getter_access_tracker["TextBox97"] = {}
		return self._TextBox97
	@TextBox97.setter
	def TextBox97(self, new_state):
		self._setter_access_tracker["TextBox97"] = {}
		global default_state
		self._TextBox97 = TextBox(new_state, default_state["TextBox97"])

	@property
	def TextBox98(self):
		self._getter_access_tracker["TextBox98"] = {}
		return self._TextBox98
	@TextBox98.setter
	def TextBox98(self, new_state):
		self._setter_access_tracker["TextBox98"] = {}
		global default_state
		self._TextBox98 = TextBox(new_state, default_state["TextBox98"])

	@property
	def Button18(self):
		self._getter_access_tracker["Button18"] = {}
		return self._Button18
	@Button18.setter
	def Button18(self, new_state):
		self._setter_access_tracker["Button18"] = {}
		global default_state
		self._Button18 = Button(new_state, default_state["Button18"])

	@property
	def Button19(self):
		self._getter_access_tracker["Button19"] = {}
		return self._Button19
	@Button19.setter
	def Button19(self, new_state):
		self._setter_access_tracker["Button19"] = {}
		global default_state
		self._Button19 = Button(new_state, default_state["Button19"])

	@property
	def TextBox104(self):
		self._getter_access_tracker["TextBox104"] = {}
		return self._TextBox104
	@TextBox104.setter
	def TextBox104(self, new_state):
		self._setter_access_tracker["TextBox104"] = {}
		global default_state
		self._TextBox104 = TextBox(new_state, default_state["TextBox104"])

	@property
	def TextBox105(self):
		self._getter_access_tracker["TextBox105"] = {}
		return self._TextBox105
	@TextBox105.setter
	def TextBox105(self, new_state):
		self._setter_access_tracker["TextBox105"] = {}
		global default_state
		self._TextBox105 = TextBox(new_state, default_state["TextBox105"])

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		global default_state
		self._Image37 = Image(new_state, default_state["Image37"])

	@property
	def Image38(self):
		self._getter_access_tracker["Image38"] = {}
		return self._Image38
	@Image38.setter
	def Image38(self, new_state):
		self._setter_access_tracker["Image38"] = {}
		global default_state
		self._Image38 = Image(new_state, default_state["Image38"])

	@property
	def TextBox106(self):
		self._getter_access_tracker["TextBox106"] = {}
		return self._TextBox106
	@TextBox106.setter
	def TextBox106(self, new_state):
		self._setter_access_tracker["TextBox106"] = {}
		global default_state
		self._TextBox106 = TextBox(new_state, default_state["TextBox106"])

	@property
	def TextBox107(self):
		self._getter_access_tracker["TextBox107"] = {}
		return self._TextBox107
	@TextBox107.setter
	def TextBox107(self, new_state):
		self._setter_access_tracker["TextBox107"] = {}
		global default_state
		self._TextBox107 = TextBox(new_state, default_state["TextBox107"])

	@property
	def Image43(self):
		self._getter_access_tracker["Image43"] = {}
		return self._Image43
	@Image43.setter
	def Image43(self, new_state):
		self._setter_access_tracker["Image43"] = {}
		global default_state
		self._Image43 = Image(new_state, default_state["Image43"])

	@property
	def Image44(self):
		self._getter_access_tracker["Image44"] = {}
		return self._Image44
	@Image44.setter
	def Image44(self, new_state):
		self._setter_access_tracker["Image44"] = {}
		global default_state
		self._Image44 = Image(new_state, default_state["Image44"])

	@property
	def Image46(self):
		self._getter_access_tracker["Image46"] = {}
		return self._Image46
	@Image46.setter
	def Image46(self, new_state):
		self._setter_access_tracker["Image46"] = {}
		global default_state
		self._Image46 = Image(new_state, default_state["Image46"])

	@property
	def Image47(self):
		self._getter_access_tracker["Image47"] = {}
		return self._Image47
	@Image47.setter
	def Image47(self, new_state):
		self._setter_access_tracker["Image47"] = {}
		global default_state
		self._Image47 = Image(new_state, default_state["Image47"])

	@property
	def Image48(self):
		self._getter_access_tracker["Image48"] = {}
		return self._Image48
	@Image48.setter
	def Image48(self, new_state):
		self._setter_access_tracker["Image48"] = {}
		global default_state
		self._Image48 = Image(new_state, default_state["Image48"])

	@property
	def Image49(self):
		self._getter_access_tracker["Image49"] = {}
		return self._Image49
	@Image49.setter
	def Image49(self, new_state):
		self._setter_access_tracker["Image49"] = {}
		global default_state
		self._Image49 = Image(new_state, default_state["Image49"])

	@property
	def Image45(self):
		self._getter_access_tracker["Image45"] = {}
		return self._Image45
	@Image45.setter
	def Image45(self, new_state):
		self._setter_access_tracker["Image45"] = {}
		global default_state
		self._Image45 = Image(new_state, default_state["Image45"])

	@property
	def TextBox109(self):
		self._getter_access_tracker["TextBox109"] = {}
		return self._TextBox109
	@TextBox109.setter
	def TextBox109(self, new_state):
		self._setter_access_tracker["TextBox109"] = {}
		global default_state
		self._TextBox109 = TextBox(new_state, default_state["TextBox109"])

	@property
	def TextBox110(self):
		self._getter_access_tracker["TextBox110"] = {}
		return self._TextBox110
	@TextBox110.setter
	def TextBox110(self, new_state):
		self._setter_access_tracker["TextBox110"] = {}
		global default_state
		self._TextBox110 = TextBox(new_state, default_state["TextBox110"])

	@property
	def Button23(self):
		self._getter_access_tracker["Button23"] = {}
		return self._Button23
	@Button23.setter
	def Button23(self, new_state):
		self._setter_access_tracker["Button23"] = {}
		global default_state
		self._Button23 = Button(new_state, default_state["Button23"])

	@property
	def Button24(self):
		self._getter_access_tracker["Button24"] = {}
		return self._Button24
	@Button24.setter
	def Button24(self, new_state):
		self._setter_access_tracker["Button24"] = {}
		global default_state
		self._Button24 = Button(new_state, default_state["Button24"])

	@property
	def TextBox114(self):
		self._getter_access_tracker["TextBox114"] = {}
		return self._TextBox114
	@TextBox114.setter
	def TextBox114(self, new_state):
		self._setter_access_tracker["TextBox114"] = {}
		global default_state
		self._TextBox114 = TextBox(new_state, default_state["TextBox114"])

	@property
	def TextBox115(self):
		self._getter_access_tracker["TextBox115"] = {}
		return self._TextBox115
	@TextBox115.setter
	def TextBox115(self, new_state):
		self._setter_access_tracker["TextBox115"] = {}
		global default_state
		self._TextBox115 = TextBox(new_state, default_state["TextBox115"])

	@property
	def TextBox116(self):
		self._getter_access_tracker["TextBox116"] = {}
		return self._TextBox116
	@TextBox116.setter
	def TextBox116(self, new_state):
		self._setter_access_tracker["TextBox116"] = {}
		global default_state
		self._TextBox116 = TextBox(new_state, default_state["TextBox116"])

	@property
	def Image53(self):
		self._getter_access_tracker["Image53"] = {}
		return self._Image53
	@Image53.setter
	def Image53(self, new_state):
		self._setter_access_tracker["Image53"] = {}
		global default_state
		self._Image53 = Image(new_state, default_state["Image53"])

	@property
	def Image54(self):
		self._getter_access_tracker["Image54"] = {}
		return self._Image54
	@Image54.setter
	def Image54(self, new_state):
		self._setter_access_tracker["Image54"] = {}
		global default_state
		self._Image54 = Image(new_state, default_state["Image54"])

	@property
	def TextBox118(self):
		self._getter_access_tracker["TextBox118"] = {}
		return self._TextBox118
	@TextBox118.setter
	def TextBox118(self, new_state):
		self._setter_access_tracker["TextBox118"] = {}
		global default_state
		self._TextBox118 = TextBox(new_state, default_state["TextBox118"])

	@property
	def TextBox119(self):
		self._getter_access_tracker["TextBox119"] = {}
		return self._TextBox119
	@TextBox119.setter
	def TextBox119(self, new_state):
		self._setter_access_tracker["TextBox119"] = {}
		global default_state
		self._TextBox119 = TextBox(new_state, default_state["TextBox119"])

	@property
	def TextBox126(self):
		self._getter_access_tracker["TextBox126"] = {}
		return self._TextBox126
	@TextBox126.setter
	def TextBox126(self, new_state):
		self._setter_access_tracker["TextBox126"] = {}
		global default_state
		self._TextBox126 = TextBox(new_state, default_state["TextBox126"])

	@property
	def TextBox127(self):
		self._getter_access_tracker["TextBox127"] = {}
		return self._TextBox127
	@TextBox127.setter
	def TextBox127(self, new_state):
		self._setter_access_tracker["TextBox127"] = {}
		global default_state
		self._TextBox127 = TextBox(new_state, default_state["TextBox127"])

	@property
	def Image58(self):
		self._getter_access_tracker["Image58"] = {}
		return self._Image58
	@Image58.setter
	def Image58(self, new_state):
		self._setter_access_tracker["Image58"] = {}
		global default_state
		self._Image58 = Image(new_state, default_state["Image58"])

	@property
	def TextBox128(self):
		self._getter_access_tracker["TextBox128"] = {}
		return self._TextBox128
	@TextBox128.setter
	def TextBox128(self, new_state):
		self._setter_access_tracker["TextBox128"] = {}
		global default_state
		self._TextBox128 = TextBox(new_state, default_state["TextBox128"])

	@property
	def TextBox129(self):
		self._getter_access_tracker["TextBox129"] = {}
		return self._TextBox129
	@TextBox129.setter
	def TextBox129(self, new_state):
		self._setter_access_tracker["TextBox129"] = {}
		global default_state
		self._TextBox129 = TextBox(new_state, default_state["TextBox129"])

	@property
	def Image59(self):
		self._getter_access_tracker["Image59"] = {}
		return self._Image59
	@Image59.setter
	def Image59(self, new_state):
		self._setter_access_tracker["Image59"] = {}
		global default_state
		self._Image59 = Image(new_state, default_state["Image59"])

	@property
	def TextBox130(self):
		self._getter_access_tracker["TextBox130"] = {}
		return self._TextBox130
	@TextBox130.setter
	def TextBox130(self, new_state):
		self._setter_access_tracker["TextBox130"] = {}
		global default_state
		self._TextBox130 = TextBox(new_state, default_state["TextBox130"])

	@property
	def TextBox131(self):
		self._getter_access_tracker["TextBox131"] = {}
		return self._TextBox131
	@TextBox131.setter
	def TextBox131(self, new_state):
		self._setter_access_tracker["TextBox131"] = {}
		global default_state
		self._TextBox131 = TextBox(new_state, default_state["TextBox131"])

	@property
	def Image60(self):
		self._getter_access_tracker["Image60"] = {}
		return self._Image60
	@Image60.setter
	def Image60(self, new_state):
		self._setter_access_tracker["Image60"] = {}
		global default_state
		self._Image60 = Image(new_state, default_state["Image60"])

	@property
	def Div79(self):
		self._getter_access_tracker["Div79"] = {}
		return self._Div79
	@Div79.setter
	def Div79(self, new_state):
		self._setter_access_tracker["Div79"] = {}
		global default_state
		self._Div79 = Div(new_state, default_state["Div79"])

	@property
	def TextBox176(self):
		self._getter_access_tracker["TextBox176"] = {}
		return self._TextBox176
	@TextBox176.setter
	def TextBox176(self, new_state):
		self._setter_access_tracker["TextBox176"] = {}
		global default_state
		self._TextBox176 = TextBox(new_state, default_state["TextBox176"])

	@property
	def TextBox177(self):
		self._getter_access_tracker["TextBox177"] = {}
		return self._TextBox177
	@TextBox177.setter
	def TextBox177(self, new_state):
		self._setter_access_tracker["TextBox177"] = {}
		global default_state
		self._TextBox177 = TextBox(new_state, default_state["TextBox177"])

	def _to_json_fields(self):
		return {
			"Flex2": self._Flex2,
			"Flex9": self._Flex9,
			"Div6": self._Div6,
			"Div7": self._Div7,
			"Flex18": self._Flex18,
			"Flex20": self._Flex20,
			"Div14": self._Div14,
			"Div13": self._Div13,
			"Flex25": self._Flex25,
			"Div15": self._Div15,
			"Flex29": self._Flex29,
			"Div19": self._Div19,
			"Flex26": self._Flex26,
			"Flex27": self._Flex27,
			"Flex28": self._Flex28,
			"Div16": self._Div16,
			"Flex36": self._Flex36,
			"Div39": self._Div39,
			"Div41": self._Div41,
			"Div42": self._Div42,
			"Flex38": self._Flex38,
			"Div31": self._Div31,
			"Div32": self._Div32,
			"Div33": self._Div33,
			"Div34": self._Div34,
			"Flex41": self._Flex41,
			"Div35": self._Div35,
			"Div36": self._Div36,
			"Div37": self._Div37,
			"Div38": self._Div38,
			"Flex44": self._Flex44,
			"Div44": self._Div44,
			"Flex45": self._Flex45,
			"Div45": self._Div45,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"Div46": self._Div46,
			"Div47": self._Div47,
			"Flex48": self._Flex48,
			"Div49": self._Div49,
			"Div50": self._Div50,
			"Flex49": self._Flex49,
			"Div51": self._Div51,
			"Div55": self._Div55,
			"Flex50": self._Flex50,
			"Div56": self._Div56,
			"Div57": self._Div57,
			"Div73": self._Div73,
			"Div76": self._Div76,
			"Div80": self._Div80,
			"Div81": self._Div81,
			"TextBox46": self._TextBox46,
			"TextBox50": self._TextBox50,
			"TextBox51": self._TextBox51,
			"Div85": self._Div85,
			"Div86": self._Div86,
			"Image2": self._Image2,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"Button1": self._Button1,
			"Button2": self._Button2,
			"TextBox17": self._TextBox17,
			"Button11": self._Button11,
			"TextBox19": self._TextBox19,
			"Button12": self._Button12,
			"TextBox20": self._TextBox20,
			"Image3": self._Image3,
			"TextBox25": self._TextBox25,
			"Image4": self._Image4,
			"Image5": self._Image5,
			"Image6": self._Image6,
			"Image7": self._Image7,
			"Button13": self._Button13,
			"Button14": self._Button14,
			"TextBox36": self._TextBox36,
			"Image8": self._Image8,
			"TextBox33": self._TextBox33,
			"TextBox34": self._TextBox34,
			"TextBox35": self._TextBox35,
			"Image9": self._Image9,
			"Image12": self._Image12,
			"TextBox43": self._TextBox43,
			"Image13": self._Image13,
			"TextBox44": self._TextBox44,
			"Image14": self._Image14,
			"TextBox45": self._TextBox45,
			"TextBox37": self._TextBox37,
			"TextBox38": self._TextBox38,
			"Button15": self._Button15,
			"Button16": self._Button16,
			"Image36": self._Image36,
			"TextBox102": self._TextBox102,
			"TextBox103": self._TextBox103,
			"Button21": self._Button21,
			"Button22": self._Button22,
			"TextBox75": self._TextBox75,
			"TextBox76": self._TextBox76,
			"Image28": self._Image28,
			"TextBox77": self._TextBox77,
			"TextBox78": self._TextBox78,
			"TextBox79": self._TextBox79,
			"Image29": self._Image29,
			"TextBox80": self._TextBox80,
			"TextBox81": self._TextBox81,
			"TextBox82": self._TextBox82,
			"Image30": self._Image30,
			"TextBox83": self._TextBox83,
			"TextBox84": self._TextBox84,
			"TextBox85": self._TextBox85,
			"Image31": self._Image31,
			"TextBox86": self._TextBox86,
			"TextBox87": self._TextBox87,
			"Image32": self._Image32,
			"TextBox88": self._TextBox88,
			"TextBox89": self._TextBox89,
			"TextBox90": self._TextBox90,
			"Image33": self._Image33,
			"TextBox91": self._TextBox91,
			"TextBox92": self._TextBox92,
			"TextBox93": self._TextBox93,
			"Image34": self._Image34,
			"TextBox94": self._TextBox94,
			"TextBox95": self._TextBox95,
			"TextBox96": self._TextBox96,
			"Image35": self._Image35,
			"TextBox97": self._TextBox97,
			"TextBox98": self._TextBox98,
			"Button18": self._Button18,
			"Button19": self._Button19,
			"TextBox104": self._TextBox104,
			"TextBox105": self._TextBox105,
			"Image37": self._Image37,
			"Image38": self._Image38,
			"TextBox106": self._TextBox106,
			"TextBox107": self._TextBox107,
			"Image43": self._Image43,
			"Image44": self._Image44,
			"Image46": self._Image46,
			"Image47": self._Image47,
			"Image48": self._Image48,
			"Image49": self._Image49,
			"Image45": self._Image45,
			"TextBox109": self._TextBox109,
			"TextBox110": self._TextBox110,
			"Button23": self._Button23,
			"Button24": self._Button24,
			"TextBox114": self._TextBox114,
			"TextBox115": self._TextBox115,
			"TextBox116": self._TextBox116,
			"Image53": self._Image53,
			"Image54": self._Image54,
			"TextBox118": self._TextBox118,
			"TextBox119": self._TextBox119,
			"TextBox126": self._TextBox126,
			"TextBox127": self._TextBox127,
			"Image58": self._Image58,
			"TextBox128": self._TextBox128,
			"TextBox129": self._TextBox129,
			"Image59": self._Image59,
			"TextBox130": self._TextBox130,
			"TextBox131": self._TextBox131,
			"Image60": self._Image60,
			"Div79": self._Div79,
			"TextBox176": self._TextBox176,
			"TextBox177": self._TextBox177,
			}


class FlexstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.flexDirection: str = get_defined_value(state, def_state, "flexDirection")
		self.alignItems: str = get_defined_value(state, def_state, "alignItems")
		self.justifyContent: str = get_defined_value(state, def_state, "justifyContent")
		self.flexWrap: str = get_defined_value(state, def_state, "flexWrap")
		self.alignContent: str = get_defined_value(state, def_state, "alignContent")
		self.rowGap: str = get_defined_value(state, def_state, "rowGap")
		self.columnGap: str = get_defined_value(state, def_state, "columnGap")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def flexDirection(self):
		self._getter_access_tracker["flexDirection"] = {}
		return self._flexDirection
	@flexDirection.setter
	def flexDirection(self, state):
		self._setter_access_tracker["flexDirection"] = {}
		self._flexDirection = state
	@property
	def alignItems(self):
		self._getter_access_tracker["alignItems"] = {}
		return self._alignItems
	@alignItems.setter
	def alignItems(self, state):
		self._setter_access_tracker["alignItems"] = {}
		self._alignItems = state
	@property
	def justifyContent(self):
		self._getter_access_tracker["justifyContent"] = {}
		return self._justifyContent
	@justifyContent.setter
	def justifyContent(self, state):
		self._setter_access_tracker["justifyContent"] = {}
		self._justifyContent = state
	@property
	def flexWrap(self):
		self._getter_access_tracker["flexWrap"] = {}
		return self._flexWrap
	@flexWrap.setter
	def flexWrap(self, state):
		self._setter_access_tracker["flexWrap"] = {}
		self._flexWrap = state
	@property
	def alignContent(self):
		self._getter_access_tracker["alignContent"] = {}
		return self._alignContent
	@alignContent.setter
	def alignContent(self, state):
		self._setter_access_tracker["alignContent"] = {}
		self._alignContent = state
	@property
	def rowGap(self):
		self._getter_access_tracker["rowGap"] = {}
		return self._rowGap
	@rowGap.setter
	def rowGap(self, state):
		self._setter_access_tracker["rowGap"] = {}
		self._rowGap = state
	@property
	def columnGap(self):
		self._getter_access_tracker["columnGap"] = {}
		return self._columnGap
	@columnGap.setter
	def columnGap(self, state):
		self._setter_access_tracker["columnGap"] = {}
		self._columnGap = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"flexDirection": self._flexDirection,
			"alignItems": self._alignItems,
			"justifyContent": self._justifyContent,
			"flexWrap": self._flexWrap,
			"alignContent": self._alignContent,
			"rowGap": self._rowGap,
			"columnGap": self._columnGap,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Flex:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: FlexstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = FlexstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class DivstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Div:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: DivstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = DivstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class TextBoxstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class TextBoxcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class TextBox:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: TextBoxstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: TextBoxcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = TextBoxstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = TextBoxcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ImagestylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ImagecustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alt: str = get_defined_value(state, def_state, "alt")
		self.src: str = get_defined_value(state, def_state, "src")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alt(self):
		self._getter_access_tracker["alt"] = {}
		return self._alt
	@alt.setter
	def alt(self, state):
		self._setter_access_tracker["alt"] = {}
		self._alt = state
	@property
	def src(self):
		self._getter_access_tracker["src"] = {}
		return self._src
	@src.setter
	def src(self, state):
		self._setter_access_tracker["src"] = {}
		self._src = state
	def _to_json_fields(self):
		return {
			"alt": self._alt,
			"src": self._src,
			}


class Image:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ImagestylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ImagecustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ImagestylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ImagecustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ButtonstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ButtoncustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class Button:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ButtonstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ButtoncustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ButtonstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ButtoncustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

