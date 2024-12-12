# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Photoscan",
    "author" : "CGMatter", 
    "description" : "Photoscans a image data-set right in blender.",
    "blender" : (4, 3, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import os


addon_keymaps = {}
_icons = None
class SNA_PT_PHOTOSCAN_82011(bpy.types.Panel):
    bl_label = 'Photoscan'
    bl_idname = 'SNA_PT_PHOTOSCAN_82011'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Photoscan'
    bl_order = 1
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout
        layout.template_icon(icon_value=411, scale=1.0)

    def draw(self, context):
        layout = self.layout
        col_B6405 = layout.column(heading='', align=False)
        col_B6405.alert = False
        col_B6405.enabled = True
        col_B6405.active = True
        col_B6405.use_property_split = False
        col_B6405.use_property_decorate = False
        col_B6405.scale_x = 1.0
        col_B6405.scale_y = 1.0
        col_B6405.alignment = 'Expand'.upper()
        col_B6405.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_D05EF = col_B6405.column(heading='', align=False)
        col_D05EF.alert = (bpy.context.scene.sna_path == '')
        col_D05EF.enabled = True
        col_D05EF.active = True
        col_D05EF.use_property_split = False
        col_D05EF.use_property_decorate = False
        col_D05EF.scale_x = 1.0
        col_D05EF.scale_y = 1.25
        col_D05EF.alignment = 'Expand'.upper()
        col_D05EF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_D05EF.prop(bpy.context.scene, 'sna_path', text='', icon_value=0, emboss=True)
        split_B77A3 = col_B6405.split(factor=0.5, align=True)
        split_B77A3.alert = False
        split_B77A3.enabled = True
        split_B77A3.active = True
        split_B77A3.use_property_split = False
        split_B77A3.use_property_decorate = False
        split_B77A3.scale_x = 1.0
        split_B77A3.scale_y = 1.0
        split_B77A3.alignment = 'Expand'.upper()
        if not True: split_B77A3.operator_context = "EXEC_DEFAULT"
        col_F1CEF = split_B77A3.column(heading='', align=True)
        col_F1CEF.alert = False
        col_F1CEF.enabled = True
        col_F1CEF.active = True
        col_F1CEF.use_property_split = False
        col_F1CEF.use_property_decorate = False
        col_F1CEF.scale_x = 1.0
        col_F1CEF.scale_y = 2.0
        col_F1CEF.alignment = 'Expand'.upper()
        col_F1CEF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_F1CEF.operator('sna.operator001_6aad1', text=bpy.context.scene.sna_quality, icon_value=212, emboss=True, depress=False)
        col_B9C5B = split_B77A3.column(heading='', align=True)
        col_B9C5B.alert = False
        col_B9C5B.enabled = True
        col_B9C5B.active = True
        col_B9C5B.use_property_split = False
        col_B9C5B.use_property_decorate = False
        col_B9C5B.scale_x = 1.0
        col_B9C5B.scale_y = 1.0
        col_B9C5B.alignment = 'Expand'.upper()
        col_B9C5B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_B9C5B.prop(bpy.context.scene, 'sna_sparse', text='Sparse', icon_value=250, emboss=True)
        col_B9C5B.prop(bpy.context.scene, 'sna_dense', text='Dense', icon_value=124, emboss=True)
        col_3E37C = layout.column(heading='', align=False)
        col_3E37C.alert = False
        col_3E37C.enabled = True
        col_3E37C.active = (bpy.context.scene.sna_path != '')
        col_3E37C.use_property_split = False
        col_3E37C.use_property_decorate = False
        col_3E37C.scale_x = 1.0
        col_3E37C.scale_y = 2.0
        col_3E37C.alignment = 'Expand'.upper()
        col_3E37C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        split_39317 = col_3E37C.split(factor=0.25, align=True)
        split_39317.alert = False
        split_39317.enabled = True
        split_39317.active = True
        split_39317.use_property_split = False
        split_39317.use_property_decorate = False
        split_39317.scale_x = 1.0
        split_39317.scale_y = 1.0
        split_39317.alignment = 'Expand'.upper()
        if not True: split_39317.operator_context = "EXEC_DEFAULT"
        op = split_39317.operator('sna.operator003_53c29', text='', icon_value=128, emboss=True, depress=False)
        op = split_39317.operator('sna.operator_74599', text='Photoscan', icon_value=0, emboss=True, depress=False)


class SNA_OT_Operator_74599(bpy.types.Operator):
    bl_idname = "sna.operator_74599"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if not os.path.exists(os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction')):
            os.mkdir(os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction'))
        folder_path = os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction')
        image_path = bpy.path.abspath(bpy.context.scene.sna_path)
        import shutil
        try:
            shutil.copytree(image_path, os.path.join(folder_path, "reconstruction_images"))
            print("Folder copied successfully")
        except FileNotFoundError:
            print(f"Source folder not found: {image_path}")
        except PermissionError:
            print("Permission denied. Check your permissions.")
        except Exception as e:
            print(f"An error occurred: {e}")
        colmap_path = os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'colmap-x64-windows-cuda'),'COLMAP.bat')
        glomap_path = os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'glomap-x64-windows'),'bin','glomap.exe')
        openmvs_interface_path = os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'OpenMVS_Windows_x64'),'InterfaceCOLMAP.exe')
        openmvs_densify_path = os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'OpenMVS_Windows_x64'),'DensifyPointCloud.exe')
        openmvs_reconstruct_mesh_path = os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'OpenMVS_Windows_x64'),'ReconstructMesh.exe')
        working_path = bpy.path.abspath(os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction'))
        quality = bpy.context.scene.sna_quality
        dense = bpy.context.scene.sna_dense
        import subprocess
        import shutil

        def create_folders(working_path):
            os.makedirs(os.path.join(working_path, "sparse"), exist_ok=True)
            os.makedirs(os.path.join(working_path, "images"), exist_ok=True)
            for x in range(10):
                print("Created folders!")

        def run_colmap_database_creator(colmap_path, database_path):
            try:
                command = [
                    colmap_path,
                    "database_creator",
                    "--database_path", database_path
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Database created!")
            except subprocess.CalledProcessError as e:
                print(f"Error running COLMAP: {e}")

        def run_colmap_feature_extractor(colmap_path, database_path, image_path):
            try:
                command = [
                    colmap_path,
                    "feature_extractor",
                    "--database_path", database_path,
                    "--image_path", image_path,
                    "--ImageReader.single_camera", "1",
                    "--ImageReader.camera_model", "PINHOLE"
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Features extracted successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error running COLMAP: {e}")

        def run_colmap_exhaustive_matcher(colmap_path, database_path):
            try:
                command = [
                    colmap_path,
                    "exhaustive_matcher",
                    "--database_path", database_path
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Exhaustive matching completed!")
            except subprocess.CalledProcessError as e:
                print(f"Error running COLMAP: {e}")

        def run_glomap_mapper(glomap_path, database_path, image_path, output_path):
            try:
                command = [
                    glomap_path,
                    "mapper",
                    "--database_path", database_path,
                    "--image_path", image_path,
                    "--output_path", output_path
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Camera mapping completed!")
            except subprocess.CalledProcessError as e:
                print(f"Error running GLOMAP: {e}")

        def export_sparse_cloud_as_ply(colmap_path, input_path, output_file):
            try:
                command = [
                    colmap_path,
                    "model_converter",
                    "--input_path", input_path,
                    "--output_path", output_file,
                    "--output_type", "PLY"
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Sparse cloud exported!")
            except subprocess.CalledProcessError as e:
                print(f"Error exporting sparse cloud: {e}")

        def run_colmap_model_converter(colmap_path, input_path, output_path):
            try:
                command = [
                    colmap_path,
                    "model_converter",
                    "--input_path", input_path,
                    "--output_path", output_path,
                    "--output_type", "TXT"
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Converted to TXT!")
            except subprocess.CalledProcessError as e:
                print(f"Error converting model: {e}")

        def run_colmap_image_undistorter(colmap_path, image_path, input_path, output_path):
            try:
                command = [
                    colmap_path,
                    "image_undistorter",
                    "--image_path", image_path,
                    "--input_path", input_path,
                    "--output_path", output_path,
                    "--output_type", "COLMAP"
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Image undistortion complete!")
            except subprocess.CalledProcessError as e:
                print(f"Error undistorting images: {e}")

        def run_openmvs_interface(openmvs_path, image_folder, input_path, output_file):
            try:
                command = [
                    openmvs_path,
                    "--image-folder", image_folder,
                    "-i", input_path,
                    "-o", output_file
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("InterfaceCOLMAP completed.")
            except subprocess.CalledProcessError as e:
                print(f"Error running OpenMVS: {e}")

        def run_openmvs_densify(openmvs_path, working_folder, input_file, output_file):
            try:
                command = [
                    openmvs_path,
                    "--working-folder", working_folder,
                    "--archive-type", "-1",
                    "-i", input_file,
                    "-o", output_file,
                "--resolution-level", level
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Dense cloud created!")
            except subprocess.CalledProcessError as e:
                print(f"Error during densification: {e}")

        def run_openmvs_reconstruct_mesh(openmvs_path, working_folder, input_file, output_file):
            try:
                command = [
                    openmvs_path,
                    "--working-folder", working_folder,
                    "-i", input_file,
                    "-o", output_file
                ]
                subprocess.run(command, check=True)
                for x in range(10):
                    print("Mesh reconstruction completed!")
            except subprocess.CalledProcessError as e:
                print(f"Error during mesh reconstruction: {e}")

        def main():
            database_path = os.path.join(working_path, "database.db")
            image_path = os.path.join(working_path, "reconstruction_images")
            sparse_output_path = os.path.join(working_path, "sparse_model")
            sparse_ply_file = os.path.join(working_path, "sparse_cloud.ply")
            undistorted_output_path = os.path.join(working_path, "images")
            mvs_output_file = os.path.join(working_path, "model_colmap.mvs")
            densified_output_file = os.path.join(working_path, "model_dense.mvs")
            mesh_output_file = os.path.join(working_path, "model_dense_mesh.ply")
            create_folders(working_path)
            run_colmap_database_creator(colmap_path, database_path)
            run_colmap_feature_extractor(colmap_path, database_path, image_path)
            run_colmap_exhaustive_matcher(colmap_path, database_path)
            run_glomap_mapper(glomap_path, database_path, image_path, sparse_output_path)
            export_sparse_cloud_as_ply(colmap_path, os.path.join(sparse_output_path, "0"), sparse_ply_file)
            if dense == True:
                run_colmap_model_converter(colmap_path, os.path.join(sparse_output_path, "0"), os.path.join(working_path, "sparse"))
                run_colmap_image_undistorter(colmap_path, image_path, os.path.join(sparse_output_path, "0"), undistorted_output_path)
                run_openmvs_interface(openmvs_interface_path, os.path.join(undistorted_output_path, "images"), working_path, mvs_output_file)
                run_openmvs_densify(openmvs_densify_path, working_path, mvs_output_file, densified_output_file)
                run_openmvs_reconstruct_mesh(openmvs_reconstruct_mesh_path, working_path, densified_output_file, mesh_output_file)
        if quality == "Low":
            level = "2"
        elif quality == "Medium":
            level = "1"
        elif quality == "High":
            level = "0"
        main()
        if bpy.context.scene.sna_sparse:
            bpy.ops.wm.ply_import(filepath=os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction')),'sparse_cloud.ply'))
        if bpy.context.scene.sna_dense:
            bpy.ops.wm.ply_import(filepath=os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(bpy.data.filepath), 'reconstruction')),'model_dense_mesh.ply'))
        folder_path = os.path.join(os.path.dirname(bpy.data.filepath),'reconstruction')
        import shutil

        def delete_folder(folder_path):
            try:
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                    print(f"The folder '{folder_path}' has been deleted successfully.")
                else:
                    print(f"The folder '{folder_path}' does not exist.")
            except PermissionError:
                print(f"You don't have permission to delete the folder '{folder_path}'.")
            except Exception as e:
                print(f"An error occurred while deleting the folder '{folder_path}': {str(e)}")
        delete_folder(folder_path)
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        layout.label(text='Reconstructing in ' + bpy.context.scene.sna_quality + ' quality.', icon_value=0)
        split_144A9 = layout.split(factor=0.10000000149011612, align=True)
        split_144A9.alert = False
        split_144A9.enabled = True
        split_144A9.active = True
        split_144A9.use_property_split = False
        split_144A9.use_property_decorate = False
        split_144A9.scale_x = 1.0
        split_144A9.scale_y = 1.0
        split_144A9.alignment = 'Expand'.upper()
        if not True: split_144A9.operator_context = "EXEC_DEFAULT"
        op = split_144A9.operator('sna.operator003_53c29', text='', icon_value=128, emboss=True, depress=False)
        split_144A9.label(text='Use the console to monitor progress.', icon_value=0)
        col_4C92F = layout.column(heading='', align=False)
        col_4C92F.alert = True
        col_4C92F.enabled = True
        col_4C92F.active = True
        col_4C92F.use_property_split = False
        col_4C92F.use_property_decorate = False
        col_4C92F.scale_x = 1.0
        col_4C92F.scale_y = 1.0
        col_4C92F.alignment = 'Expand'.upper()
        col_4C92F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_4C92F.label(text='Console window might spawn in background!', icon_value=0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)


class SNA_MT_15DB6(bpy.types.Menu):
    bl_idname = "SNA_MT_15DB6"
    bl_label = "Quality"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        op = layout.operator('sna.operator002_2f88d', text='Low', icon_value=0, emboss=True, depress=False)
        op.sna_choice = 'Low'
        op = layout.operator('sna.operator002_2f88d', text='Medium', icon_value=0, emboss=True, depress=False)
        op.sna_choice = 'Medium'
        op = layout.operator('sna.operator002_2f88d', text='High', icon_value=0, emboss=True, depress=False)
        op.sna_choice = 'High'


class SNA_OT_Operator001_6Aad1(bpy.types.Operator):
    bl_idname = "sna.operator001_6aad1"
    bl_label = "Operator.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.wm.call_menu(name="SNA_MT_15DB6")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator002_2F88D(bpy.types.Operator):
    bl_idname = "sna.operator002_2f88d"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_choice: bpy.props.StringProperty(name='choice', description='', default='Low', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_quality = self.sna_choice
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator003_53C29(bpy.types.Operator):
    bl_idname = "sna.operator003_53c29"
    bl_label = "Operator.003"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.wm.console_toggle('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_AddonPreferences_E1F36(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        if not (False):
            layout = self.layout 
            col_CD43C = layout.column(heading='', align=False)
            col_CD43C.alert = True
            col_CD43C.enabled = True
            col_CD43C.active = True
            col_CD43C.use_property_split = False
            col_CD43C.use_property_decorate = False
            col_CD43C.scale_x = 1.0
            col_CD43C.scale_y = 1.0
            col_CD43C.alignment = 'Expand'.upper()
            col_CD43C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_CD43C.label(text='You must save your .blend first before running!', icon_value=0)
            split_E4909 = layout.split(factor=0.4722222685813904, align=False)
            split_E4909.alert = False
            split_E4909.enabled = True
            split_E4909.active = True
            split_E4909.use_property_split = False
            split_E4909.use_property_decorate = False
            split_E4909.scale_x = 1.0
            split_E4909.scale_y = 1.0
            split_E4909.alignment = 'Expand'.upper()
            if not True: split_E4909.operator_context = "EXEC_DEFAULT"
            split_E4909.label(text='Path should lead to your image folder!', icon_value=0)
            split_E4909.prop(bpy.context.scene, 'sna_path', text='', icon_value=0, emboss=True)
            split_C67CC = layout.split(factor=0.8333333730697632, align=False)
            split_C67CC.alert = False
            split_C67CC.enabled = True
            split_C67CC.active = True
            split_C67CC.use_property_split = False
            split_C67CC.use_property_decorate = False
            split_C67CC.scale_x = 1.0
            split_C67CC.scale_y = 1.0
            split_C67CC.alignment = 'Expand'.upper()
            if not True: split_C67CC.operator_context = "EXEC_DEFAULT"
            split_C67CC.label(text='The console button is great for seeing progress! Use it! UI will lock!', icon_value=0)
            op = split_C67CC.operator('sna.operator003_53c29', text='', icon_value=128, emboss=True, depress=False)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_path = bpy.props.StringProperty(name='path', description='', default='', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_quality = bpy.props.StringProperty(name='quality', description='', default='Low', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_sparse = bpy.props.BoolProperty(name='sparse', description='', default=True)
    bpy.types.Scene.sna_dense = bpy.props.BoolProperty(name='dense', description='', default=True)
    bpy.utils.register_class(SNA_PT_PHOTOSCAN_82011)
    bpy.utils.register_class(SNA_OT_Operator_74599)
    bpy.utils.register_class(SNA_MT_15DB6)
    bpy.utils.register_class(SNA_OT_Operator001_6Aad1)
    bpy.utils.register_class(SNA_OT_Operator002_2F88D)
    bpy.utils.register_class(SNA_OT_Operator003_53C29)
    bpy.utils.register_class(SNA_AddonPreferences_E1F36)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_dense
    del bpy.types.Scene.sna_sparse
    del bpy.types.Scene.sna_quality
    del bpy.types.Scene.sna_path
    bpy.utils.unregister_class(SNA_PT_PHOTOSCAN_82011)
    bpy.utils.unregister_class(SNA_OT_Operator_74599)
    bpy.utils.unregister_class(SNA_MT_15DB6)
    bpy.utils.unregister_class(SNA_OT_Operator001_6Aad1)
    bpy.utils.unregister_class(SNA_OT_Operator002_2F88D)
    bpy.utils.unregister_class(SNA_OT_Operator003_53C29)
    bpy.utils.unregister_class(SNA_AddonPreferences_E1F36)
