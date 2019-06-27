import sys
import os
import xml.etree.ElementTree as ET
import xmltodict


class XoscParser(object):
    """
    """
    def __init__ (self, xoscfile):
        self.xoscfile = ET.parse(xoscfile)
        self.xosc_root = self.xoscfile.getroot()
        print(self.xosc_root)
		# self.storyBoard = self.StoryBoard()

    def get_all_tags (self):
        self.tags = []
        for child in self.xosc_root:
            self.tags.append(child.tag)
        return self.tags

    def check_node_got_child (self, child_node):
        tree_tag = self.xosc_root.find(child_node)
        if child_node in self.tags:
            if not bool(tree_tag.attrib):
                return True
        return False

    def get_children_of_node (self, node, node_children={}):
        node = self.xosc_root.find(node)
        if node:
            for child in node:
                node_children[child.tag] = child.attrib
        return node_children

class StoryBoard(XoscParser):
    def __init__(self, file):
            print("Story board called")
            super(StoryBoard, self).__init__(file)
            self.story_node = None
            # print(self.xosc_root)

    def get_storyBoard(self):
        """
        """
        self.story_node = self.get_children_of_node("Storyboard")
        return self.story_node

    def get_story(self):
        if not self.story_node:
            self.story_node = self.get_storyBoard()
        print(self.story_node)
        self.story_name = self.story_node['Story']['name']
        self.story_owner = self.story_node['Story']['owner']
        return self.story_name, self.story_owner

    def get_inits(self):
        """
        """
        inits = {}
        self.Init_node = self.xosc_root.find("Storyboard/Init")

        xmlstr = ET.tostring(self.Init_node)
        data_dict = dict(xmltodict.parse(xmlstr))
        # print(data_dict.values())
        in_init = list(data_dict.values())[0]
        # print(len(in_init))
        # print("The Init keys {} \n \n ".format(in_init.keys()))
        action = list(in_init.values())[0]
        # print(type(action))
        # print("Keys Inside Init {} \n \n".format(action.keys()))
        private = list(action.values())[0]
        print("Total number of actors including ego {} \n \n ".format(len(private)))
        # print(private[0].keys())
        # print(private[1].keys())
        ego = private[0]
        other = private[1]
        for i in range(len(private)):
            actor = private[i]

            # obj = actor['@object']
            longitudinal = list(actor['Action'])[0]
            speed = list(longitudinal.values())[0]
            dynamics = list(speed.values())[0]
            # print("actor ------> \n {0}\n longitudinal--->\n{1}\nspeed--->\n{2}\ndynamics---->\n{3}\n ".format(i, longitudinal, speed, dynamics))
            print((dynamics['Target']['Absolute']['@value']))
            break


        # print("Keys in ego vehicle {}".format(ego.keys()))

        # ego_object = ego['@object']
        # ego_action = list(ego['Action'])
        # # print((ego_action))
        # longitudinal = ego_action[0]
        # # print(longitudinal.values())
        # speed = list(longitudinal.values())[0]
        # # print(speed.keys())
        # dynamics = list(speed.values())[0]
        # # print(dynamics['Target']['Absolute']['@value'])


    def get_endCondition(self):
        """
        """
        pass

class ParameterDeclaration(XoscParser):
    def __init__(self, file):
            print("Declared Parameter called")
            super(ParameterDeclaration, self).__init__(file)

    def get_declaredParameters(self):
        print("Implementation of Parameter Deceleration")
        # print(self.check_node_got_child("ParameterDeclaration"))
        # param_node = self.get_children_of_node("ParameterDeclaration")
        # print(param_node)
        pass

class Catalogs(XoscParser):
    def __init__(self, file):
            print("Catalogs is called")
            super(Catalogs, self).__init__(file)

    def get_catalogs(self):
        print(self.check_node_got_child("Catalogs"))
        catlog_node = self.get_children_of_node("Catalogs")
        print(catlog_node)
        pass

class RoadNetwork(XoscParser):
    def __init__(self, file):
            print("Road Network is called")
            super(RoadNetwork, self).__init__(file)

    def get_roadNetwork(self):
        print(self.check_node_got_child("RoadNetwork"))
        road_network_node = self.get_children_of_node("RoadNetwork")
        print(road_network_node)
        pass

class Entities(XoscParser):
    def __init__(self, file):
            print("Entites called")
            super(Entities, self).__init__(file)

    def get_entities(self):
        print(self.check_node_got_child("Entities"))
        entities_node = self.get_children_of_node("Entities")
        pass

class Details(XoscParser):
    def __init__(self, file):
        print("Asking for Details")
        super(Details, file).__init__(file)

    def get_fileDescription(self):
        pass


if __name__ == "__main__":
    my_xml = XoscParser('EgoLaneChangeWithColumnOnRightLanes.xosc')

    my_tags = my_xml.get_all_tags()
    # print(my_tags)
    unknown = StoryBoard('EgoLaneChangeWithColumnOnRightLanes.xosc')
    # print(unknown.get_story())
    unknown.get_inits()


