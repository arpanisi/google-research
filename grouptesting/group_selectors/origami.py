# coding=utf-8
# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Defines Origami group strategies (only for some input sizes)."""

import itertools

import gin
import jax
import jax.numpy as np
import numpy as onp
import scipy.special
from grouptesting.group_selectors import group_selector


def origami_xl5():
  new_groups = onp.zeros((94, 271))
  new_groups[0, [0, 22, 46, 80, 101, 134, 180, 207, 220, 229, 245, 270]] = 1
  new_groups[1, [31, 33, 38, 46, 77, 86, 100, 102, 105, 107, 129, 159, 219, 248, 262]] = 1
  new_groups[2, [0, 8, 14, 16, 18, 20, 57, 74, 79, 120, 223, 238, 249, 269]] = 1
  new_groups[3, [6, 12, 27, 85, 98, 111, 121, 141, 171, 175, 177, 179, 186, 205, 206]] = 1
  new_groups[4, [6, 11, 29, 38, 45, 47, 68, 76, 126, 147, 149, 169, 173, 210, 215]] = 1
  new_groups[5, [12, 35, 51, 60, 115, 122, 133, 151, 173, 238, 241, 270]] = 1
  new_groups[6, [2, 19, 55, 59, 76, 116, 127, 130, 141, 146, 190, 202, 204, 244, 262]] = 1
  new_groups[7, [46, 52, 68, 97, 110, 117, 118, 156, 160, 178, 196, 214, 236, 238]] = 1
  new_groups[8, [24, 60, 102, 116, 125, 137, 166, 214, 218, 227, 253, 259, 261]] = 1
  new_groups[9, [43, 63, 77, 138, 147, 153, 158, 164, 167, 184, 205, 223, 240, 250, 270]] = 1
  new_groups[10, [10, 12, 29, 41, 54, 66, 87, 102, 138, 146, 208, 236, 237, 247, 255]] = 1
  new_groups[11, [56, 106, 119, 129, 137, 160, 163, 184, 186, 234, 235, 245, 246, 257, 269]] = 1
  new_groups[12, [27, 51, 74, 78, 96, 126, 130, 140, 152, 188, 198, 231, 236, 243, 248]] = 1
  new_groups[13, [41, 74, 91, 100, 118, 128, 139, 147, 157, 181, 192, 197, 202, 213, 253]] = 1
  new_groups[14, [14, 23, 30, 61, 67, 83, 95, 102, 113, 121, 136, 162, 190, 210, 213]] = 1
  new_groups[15, [1, 13, 24, 27, 89, 114, 135, 139, 143, 146, 167, 170, 194, 207, 210]] = 1
  new_groups[16, [2, 26, 58, 104, 121, 133, 149, 167, 182, 183, 187, 188, 199, 253, 269]] = 1
  new_groups[17, [9, 10, 28, 34, 51, 90, 94, 101, 121, 124, 131, 144, 170, 197, 224]] = 1
  new_groups[18, [22, 23, 42, 50, 53, 65, 88, 96, 115, 142, 172, 177, 197, 246, 264]] = 1
  new_groups[19, [63, 79, 101, 110, 128, 136, 174, 176, 186, 195, 204, 209, 230, 248]] = 1
  new_groups[20, [4, 18, 44, 53, 94, 104, 106, 107, 151, 157, 196, 205, 210, 216, 225]] = 1
  new_groups[21, [13, 49, 54, 56, 71, 73, 84, 94, 95, 110, 123, 182, 218, 267, 268]] = 1
  new_groups[22, [44, 58, 76, 82, 86, 91, 114, 142, 165, 189, 214, 243, 251, 267, 270]] = 1
  new_groups[23, [14, 33, 75, 78, 93, 134, 167, 179, 193, 197, 201, 212, 214, 239, 242]] = 1
  new_groups[24, [7, 10, 27, 52, 62, 76, 80, 83, 104, 112, 168, 209, 223, 234, 258]] = 1
  new_groups[25, [3, 19, 23, 37, 75, 77, 82, 108, 137, 144, 175, 211, 220, 249]] = 1
  new_groups[26, [3, 21, 51, 87, 98, 145, 150, 172, 178, 201, 204, 207, 223, 235, 253]] = 1
  new_groups[27, [1, 7, 35, 39, 45, 120, 123, 171, 183, 212, 220, 227, 246, 262, 263]] = 1
  new_groups[28, [39, 44, 47, 72, 90, 109, 132, 160, 177, 195, 223, 231, 254, 255, 259]] = 1
  new_groups[29, [0, 3, 25, 35, 40, 49, 69, 140, 153, 170, 179, 189, 199, 255]] = 1
  new_groups[30, [3, 9, 36, 57, 72, 73, 83, 106, 111, 147, 180, 194, 208, 244, 248]] = 1
  new_groups[31, [10, 16, 48, 81, 141, 143, 149, 158, 178, 181, 185, 189, 211, 241, 261]] = 1
  new_groups[32, [64, 81, 82, 89, 99, 126, 136, 157, 166, 179, 208, 222, 262, 266]] = 1
  new_groups[33, [5, 15, 20, 22, 24, 95, 104, 119, 126, 154, 175, 178, 202, 212, 219]] = 1
  new_groups[34, [9, 16, 43, 54, 59, 118, 134, 188, 209, 219, 252, 254, 265]] = 1
  new_groups[35, [41, 49, 62, 113, 131, 137, 155, 188, 206, 232, 238, 242, 262]] = 1
  new_groups[36, [8, 27, 37, 38, 63, 88, 93, 151, 199, 202, 218, 221, 235, 252, 266]] = 1
  new_groups[37, [21, 40, 45, 58, 92, 103, 111, 184, 190, 211, 225, 236, 239, 254, 266]] = 1
  new_groups[38, [38, 55, 71, 90, 111, 133, 136, 142, 153, 185, 193, 198, 207, 227, 265]] = 1
  new_groups[39, [14, 28, 150, 173, 182, 189, 205, 217, 226, 227, 236]] = 1
  new_groups[40, [20, 37, 96, 97, 132, 150, 164, 169, 170, 183, 186, 200, 213, 216, 244]] = 1
  new_groups[41, [9, 33, 35, 41, 65, 98, 109, 119, 143, 190, 218, 229, 249, 250, 258]] = 1
  new_groups[42, [2, 8, 46, 54, 61, 103, 119, 135, 147, 148, 172, 176, 185, 224, 232]] = 1
  new_groups[43, [0, 10, 15, 67, 89, 93, 132, 142, 171, 188, 191, 215, 225, 257, 260]] = 1
  new_groups[44, [2, 21, 25, 30, 65, 81, 112, 134, 154, 164, 173, 198, 221, 230, 237]] = 1
  new_groups[45, [5, 8, 25, 42, 85, 99, 100, 122, 123, 214, 225, 231, 234, 240]] = 1
  new_groups[46, [19, 29, 57, 70, 88, 101, 133, 135, 152, 160, 162, 165, 200, 219, 242]] = 1
  new_groups[47, [47, 53, 71, 120, 146, 154, 159, 165, 166, 203, 232, 234, 241, 250]] = 1
  new_groups[48, [5, 7, 13, 18, 48, 72, 91, 92, 96, 131, 134, 138, 199, 204, 222]] = 1
  new_groups[49, [14, 39, 53, 62, 77, 119, 125, 139, 141, 145, 200, 251, 260, 266]] = 1
  new_groups[50, [36, 49, 50, 117, 124, 146, 152, 163, 185, 209, 216, 249, 263, 266, 270]] = 1
  new_groups[51, [13, 58, 64, 65, 90, 93, 106, 113, 122, 130, 150, 158, 159, 161, 209]] = 1
  new_groups[52, [28, 43, 48, 74, 88, 122, 148, 191, 207, 216, 239, 251, 256, 259]] = 1
  new_groups[53, [21, 42, 80, 106, 120, 121, 125, 143, 153, 155, 176, 215, 217, 222, 252]] = 1
  new_groups[54, [12, 34, 39, 50, 56, 92, 100, 116, 162, 169, 176, 194, 221, 229, 243]] = 1
  new_groups[55, [24, 61, 66, 86, 88, 90, 92, 98, 99, 108, 112, 127, 128, 268, 269]] = 1
  new_groups[56, [7, 24, 26, 34, 41, 63, 67, 73, 140, 148, 163, 201, 241, 254]] = 1
  new_groups[57, [5, 19, 51, 68, 86, 177, 208, 213, 229, 233, 239, 252]] = 1
  new_groups[58, [3, 68, 95, 101, 109, 125, 130, 157, 163, 164, 206, 256, 264]] = 1
  new_groups[59, [32, 52, 61, 71, 122, 152, 157, 170, 174, 184, 212, 233, 237, 260]] = 1
  new_groups[60, [26, 31, 59, 85, 103, 138, 156, 166, 210, 220, 221, 242, 256, 260]] = 1
  new_groups[61, [8, 17, 22, 69, 70, 81, 83, 94, 186, 226, 233, 250, 254]] = 1
  new_groups[62, [17, 23, 31, 73, 79, 80, 127, 139, 160, 225, 232, 243, 247, 261, 263]] = 1
  new_groups[63, [69, 78, 82, 129, 131, 133, 169, 205, 230, 256, 258, 261, 268]] = 1
  new_groups[64, [16, 69, 105, 108, 115, 116, 126, 132, 167, 180, 196, 206, 234, 247, 267]] = 1
  new_groups[65, [84, 89, 92, 104, 105, 118, 144, 161, 165, 173, 195, 233, 235, 256, 263]] = 1
  new_groups[66, [1, 2, 18, 40, 87, 97, 100, 144, 174, 217, 241, 251, 264, 265, 268]] = 1
  new_groups[67, [9, 13, 61, 75, 85, 140, 155, 164, 168, 178, 195, 226, 246, 247, 251]] = 1
  new_groups[68, [4, 52, 70, 73, 89, 91, 145, 149, 224, 245, 249, 252, 259, 264]] = 1
  new_groups[69, [20, 32, 38, 40, 44, 78, 98, 115, 123, 139, 148, 156, 162, 187, 203]] = 1
  new_groups[70, [25, 33, 34, 43, 66, 70, 71, 82, 97, 168, 177, 192, 204, 215, 263]] = 1
  new_groups[71, [4, 12, 15, 31, 37, 47, 58, 74, 81, 110, 155, 163, 172, 180, 227]] = 1
  new_groups[72, [4, 20, 43, 60, 109, 113, 114, 127, 129, 171, 174, 185, 201, 221]] = 1
  new_groups[73, [1, 11, 33, 50, 112, 113, 148, 153, 195, 196, 202, 208, 211]] = 1
  new_groups[74, [15, 26, 46, 66, 109, 120, 131, 145, 161, 181, 184, 194, 198, 216, 267]] = 1
  new_groups[75, [6, 17, 35, 42, 44, 102, 118, 124, 130, 154, 174, 180, 182, 211, 257]] = 1
  new_groups[76, [40, 42, 47, 56, 57, 93, 107, 117, 127, 136, 138, 168, 183, 206, 224]] = 1
  new_groups[77, [30, 69, 86, 111, 123, 143, 151, 161, 166, 172, 192, 200, 257]] = 1
  new_groups[78, [31, 72, 87, 112, 135, 137, 169, 171, 181, 182, 190, 193, 203, 233]] = 1
  new_groups[79, [0, 1, 21, 32, 64, 66, 68, 72, 85, 105, 197, 200, 218, 228, 243]] = 1
  new_groups[80, [17, 64, 76, 110, 115, 125, 183, 191, 192, 193, 194, 219, 237, 240, 245]] = 1
  new_groups[81, [11, 17, 28, 36, 52, 65, 103, 107, 132, 175, 187, 222, 268]] = 1
  new_groups[82, [15, 18, 29, 39, 83, 84, 108, 114, 117, 140, 158, 187, 230, 232, 239]] = 1
  new_groups[83, [11, 32, 48, 59, 79, 95, 108, 135, 142, 159, 192, 201, 226, 229, 231]] = 1
  new_groups[84, [6, 7, 36, 37, 114, 159, 196, 198, 228, 240, 242, 261, 264, 269]] = 1
  new_groups[85, [11, 25, 54, 55, 62, 75, 96, 124, 151, 156, 158, 165, 217, 245, 253]] = 1
  new_groups[86, [30, 32, 34, 36, 45, 75, 84, 87, 128, 129, 141, 191, 199, 238, 250]] = 1
  new_groups[87, [19, 26, 48, 78, 80, 128, 150, 154, 224, 228, 246, 265]] = 1
  new_groups[88, [5, 16, 28, 30, 55, 56, 60, 63, 145, 152, 203, 215, 220, 255]] = 1
  new_groups[89, [4, 22, 29, 49, 67, 79, 105, 156, 168, 181, 222, 240, 244, 265]] = 1
  new_groups[90, [50, 59, 60, 62, 70, 84, 99, 175, 189, 193, 213, 228, 247, 248, 257]] = 1
  new_groups[91, [23, 64, 97, 107, 116, 124, 149, 155, 203, 230, 231, 235, 260]] = 1
  new_groups[92, [6, 77, 91, 94, 99, 103, 117, 161, 162, 191, 212, 217, 244, 255, 258]] = 1
  new_groups[93, [45, 53, 55, 57, 67, 144, 176, 179, 187, 226, 228, 237, 258, 259, 267]] = 1
  return np.array(new_groups, dtype=bool)


def origami_l5():
  new_groups=onp.zeros((46,68))
  new_groups[0, [1, 10, 26, 29, 52, 56, 57, 66]] = 1
  new_groups[1, [0, 6, 7, 18, 51, 57, 60, 62]] = 1
  new_groups[2, [15, 21, 25, 27, 40, 42, 52, 61]] = 1
  new_groups[3, [2, 7, 13, 14, 28, 41, 46, 48]] = 1
  new_groups[4, [0, 8, 11, 21, 28, 30, 47, 53]] = 1
  new_groups[5, [2, 16, 20, 36, 45, 55, 63, 66]] = 1
  new_groups[6, [1, 5, 8, 12, 19, 32, 33, 48]] = 1
  new_groups[7, [0, 1, 17, 22, 36, 40, 49, 50]] = 1
  new_groups[8, [17, 33, 34, 62, 66, 67]] = 1
  new_groups[9, [4, 14, 26, 27, 36, 53, 64, 67]] = 1
  new_groups[10, [3, 12, 41, 49, 52, 54, 60, 63]] = 1
  new_groups[11, [8, 38, 39, 57, 63, 64]] = 1
  new_groups[12, [18, 22, 26, 39, 46, 54, 55]] = 1
  new_groups[13, [21, 23, 29, 43, 46, 50, 67]] = 1
  new_groups[14, [2, 3, 5, 15, 22, 37, 38, 47]] = 1
  new_groups[15, [3, 10, 48, 51, 55, 61, 67]] = 1
  new_groups[16, [8, 31, 36, 37, 54, 58, 61, 65]] = 1
  new_groups[17, [7, 20, 27, 30, 32, 38]] = 1
  new_groups[18, [15, 23, 28, 32, 39, 44, 49, 66]] = 1
  new_groups[19, [4, 7, 10, 35, 47, 65]] = 1
  new_groups[20, [24, 27, 29, 31, 48, 49, 62]] = 1
  new_groups[21, [4, 16, 24, 32, 41, 50, 57]] = 1
  new_groups[22, [16, 19, 43, 47, 56, 60, 61]] = 1
  new_groups[23, [6, 16, 22, 44, 48, 52, 64, 65]] = 1
  new_groups[24, [10, 13, 27, 33, 37, 59, 63]] = 1
  new_groups[25, [1, 18, 23, 34, 38, 41, 53, 61]] = 1
  new_groups[26, [4, 12, 15, 30, 34, 46, 56, 58]] = 1
  new_groups[27, [9, 13, 17, 18, 31, 32, 47, 52]] = 1
  new_groups[28, [5, 9, 23, 25, 58, 62, 63]] = 1
  new_groups[29, [26, 30, 37, 41, 42, 45, 51]] = 1
  new_groups[30, [0, 14, 25, 29, 33, 38, 55, 65]] = 1
  new_groups[31, [4, 9, 19, 22, 28, 29, 51, 59]] = 1
  new_groups[32, [3, 6, 9, 11, 33, 36, 42, 46]] = 1
  new_groups[33, [6, 13, 19, 45, 49, 53, 58]] = 1
  new_groups[34, [14, 16, 30, 40, 54, 59]] = 1
  new_groups[35, [0, 2, 23, 35, 42, 56, 59, 64]] = 1
  new_groups[36, [5, 7, 17, 21, 45, 54, 56]] = 1
  new_groups[37, [9, 24, 35, 37, 40, 53, 60, 66]] = 1
  new_groups[38, [8, 20, 25, 26, 34, 50, 59, 60]] = 1
  new_groups[39, [2, 11, 12, 31, 40, 44, 57, 67]] = 1
  new_groups[40, [5, 11, 34, 39, 43, 51, 65]] = 1
  new_groups[41, [17, 19, 20, 24, 42, 44]] = 1
  new_groups[42, [10, 12, 18, 24, 25, 28, 43, 45]] = 1
  new_groups[43, [11, 13, 15, 50, 55, 62, 64]] = 1
  new_groups[44, [1, 6, 14, 20, 21, 31, 35, 39]] = 1
  new_groups[45, [3, 35, 43, 44, 58]] = 1
  return np.array(new_groups, dtype=bool)

def origami_l3():
  new_groups = onp.zeros((46,274))
  new_groups[0, [11, 25, 33, 80, 87, 119, 125, 126, 130, 131, 133, 162, 163, 191, 197, 199, 203, 216]] = 1
  new_groups[1, [3, 16, 26, 42, 43, 102, 129, 151, 203, 217, 218, 247, 264, 271, 272, 273]] = 1
  new_groups[2, [7, 31, 32, 36, 45, 56, 63, 70, 127, 149, 157, 178, 182, 192, 233, 239, 267, 271]] = 1
  new_groups[3, [2, 5, 45, 68, 88, 121, 130, 136, 137, 148, 165, 181, 194, 210, 212, 229, 236, 272]] = 1
  new_groups[4, [19, 30, 57, 67, 70, 76, 91, 107, 124, 131, 151, 160, 164, 167, 174, 221, 234, 240]] = 1
  new_groups[5, [3, 6, 17, 33, 72, 75, 98, 104, 157, 161, 175, 180, 181, 208, 223, 243, 253, 270]] = 1
  new_groups[6, [2, 22, 33, 34, 38, 42, 61, 128, 145, 156, 168, 169, 171, 173, 176, 193, 219, 255]] = 1
  new_groups[7, [10, 21, 47, 63, 77, 84, 95, 121, 124, 138, 169, 190, 200, 216, 238, 256, 266, 270]] = 1
  new_groups[8, [0, 13, 14, 20, 35, 48, 52, 56, 76, 85, 103, 126, 137, 171, 172, 198, 231, 249]] = 1
  new_groups[9, [34, 39, 58, 71, 73, 76, 81, 83, 120, 133, 135, 141, 143, 144, 210, 233, 253, 256]] = 1
  new_groups[10, [15, 31, 37, 41, 54, 55, 69, 73, 93, 105, 106, 107, 132, 137, 147, 163, 168, 180]] = 1
  new_groups[11, [17, 31, 38, 43, 47, 91, 112, 134, 155, 177, 204, 212, 232, 249, 252, 257, 259, 260]] = 1
  new_groups[12, [19, 26, 28, 44, 46, 50, 68, 77, 85, 109, 127, 152, 177, 180, 241, 245, 248, 262]] = 1
  new_groups[13, [8, 29, 46, 75, 95, 103, 110, 114, 193, 194, 197, 225, 230, 234, 239, 250, 257, 258]] = 1
  new_groups[14, [25, 55, 64, 71, 96, 99, 101, 111, 127, 138, 145, 161, 183, 212, 240, 244, 247, 258]] = 1
  new_groups[15, [29, 41, 49, 52, 67, 113, 115, 139, 141, 181, 192, 202, 203, 207, 211, 219, 220, 248]] = 1
  new_groups[16, [4, 32, 51, 67, 75, 92, 93, 96, 119, 122, 135, 142, 165, 177, 184, 214, 242, 263]] = 1
  new_groups[17, [9, 20, 40, 66, 87, 93, 120, 128, 136, 146, 175, 188, 211, 213, 250, 261, 262, 269]] = 1
  new_groups[18, [1, 26, 48, 69, 71, 91, 108, 140, 148, 186, 223, 224, 228, 230, 261, 267, 268]] = 1
  new_groups[19, [4, 16, 22, 40, 65, 80, 106, 109, 117, 172, 174, 205, 220, 229, 254, 256, 260, 267]] = 1
  new_groups[20, [1, 6, 10, 12, 41, 81, 86, 99, 130, 150, 151, 154, 156, 172, 195, 213, 214, 237]] = 1
  new_groups[21, [14, 18, 53, 69, 97, 117, 119, 128, 155, 179, 183, 189, 200, 218, 233, 234, 236, 237]] = 1
  new_groups[22, [23, 53, 77, 87, 105, 118, 123, 134, 149, 156, 164, 207, 210, 215, 223, 227, 231, 242]] = 1
  new_groups[23, [4, 49, 68, 70, 74, 78, 79, 98, 116, 123, 133, 154, 173, 188, 201, 224, 238, 257]] = 1
  new_groups[24, [8, 15, 34, 44, 56, 97, 100, 115, 123, 153, 160, 184, 186, 195, 209, 247, 251, 252]] = 1
  new_groups[25, [0, 6, 9, 25, 47, 65, 108, 113, 116, 153, 158, 170, 217, 221, 225, 236, 263]] = 1
  new_groups[26, [0, 11, 12, 15, 28, 36, 40, 58, 61, 84, 98, 166, 167, 215, 218, 258, 259, 265]] = 1
  new_groups[27, [59, 72, 79, 86, 94, 107, 125, 144, 145, 166, 182, 189, 190, 231, 248, 251, 260, 264]] = 1
  new_groups[28, [5, 39, 64, 95, 100, 104, 146, 152, 158, 166, 174, 187, 191, 192, 222, 228, 242, 255]] = 1
  new_groups[29, [3, 5, 27, 30, 90, 97, 116, 120, 138, 139, 142, 168, 182, 198, 226, 230, 235, 245]] = 1
  new_groups[30, [17, 36, 53, 62, 78, 81, 89, 103, 111, 131, 158, 176, 184, 196, 211, 226, 266, 272]] = 1
  new_groups[31, [13, 24, 44, 63, 65, 72, 90, 114, 135, 147, 150, 159, 187, 188, 219, 240, 268, 273]] = 1
  new_groups[32, [10, 24, 35, 38, 45, 54, 62, 83, 100, 140, 142, 164, 185, 197, 244, 254, 262, 264]] = 1
  new_groups[33, [7, 14, 30, 42, 49, 84, 88, 92, 109, 132, 134, 144, 161, 170, 187, 199, 209, 213]] = 1
  new_groups[34, [20, 27, 60, 96, 114, 140, 173, 216, 221, 222, 227, 229, 237, 241, 246, 252, 253, 265]] = 1
  new_groups[35, [8, 18, 23, 37, 79, 80, 82, 89, 92, 113, 150, 171, 206, 241, 244, 259, 261, 271]] = 1
  new_groups[36, [9, 51, 57, 59, 74, 82, 85, 88, 90, 104, 143, 195, 207, 232, 239, 254, 265, 266]] = 1
  new_groups[37, [13, 28, 55, 62, 74, 94, 108, 110, 118, 129, 155, 165, 191, 205, 209, 246, 270]] = 1
  new_groups[38, [16, 27, 46, 54, 61, 124, 136, 141, 154, 162, 170, 178, 183, 196, 206, 208, 228, 232]] = 1
  new_groups[39, [18, 48, 50, 58, 59, 64, 66, 102, 118, 122, 147, 157, 194, 196, 199, 220, 235, 238]] = 1
  new_groups[40, [1, 11, 19, 29, 82, 94, 105, 112, 121, 176, 178, 179, 185, 198, 222, 263, 269, 273]] = 1
  new_groups[41, [12, 37, 50, 60, 83, 111, 115, 126, 129, 149, 169, 189, 201, 204, 225, 268, 269]] = 1
  new_groups[42, [22, 39, 78, 101, 125, 132, 153, 185, 200, 202, 206, 214, 215, 235, 243, 246, 249, 250]] = 1
  new_groups[43, [7, 35, 57, 73, 89, 112, 117, 122, 139, 146, 159, 186, 190, 193, 201, 217, 227, 243]] = 1
  new_groups[44, [2, 21, 23, 51, 52, 86, 101, 102, 106, 110, 152, 159, 160, 162, 175, 204, 224, 226]] = 1
  new_groups[45, [21, 24, 32, 43, 60, 66, 99, 143, 148, 163, 167, 179, 202, 205, 208, 245, 251, 255]] = 1
  return np.array(new_groups, dtype=bool)

def origami_m3():
  new_groups = onp.zeros((22,70))
  new_groups[0, [4, 10, 18, 20, 34, 53, 56, 63, 67, 69]] = 1
  new_groups[1, [2, 6, 11, 27, 30, 31, 35, 56, 59, 64]] = 1
  new_groups[2, [3, 13, 23, 35, 37, 40, 45, 69]] = 1
  new_groups[3, [23, 29, 33, 41, 44, 47, 54, 56, 61, 62]] = 1
  new_groups[4, [3, 9, 10, 11, 15, 50, 52, 61, 66]] = 1
  new_groups[5, [4, 5, 8, 17, 22, 26, 32, 45, 59, 61]] = 1
  new_groups[6, [0, 16, 18, 24, 25, 26, 40, 41, 49, 50]] = 1
  new_groups[7, [1, 4, 7, 21, 31, 37, 43, 50, 57, 62]] = 1
  new_groups[8, [9, 13, 16, 27, 29, 39, 51, 57, 68]] = 1
  new_groups[9, [6, 8, 15, 33, 40, 48, 58, 63, 68]] = 1
  new_groups[10, [1, 8, 10, 12, 14, 30, 41, 55, 65]] = 1
  new_groups[11, [2, 12, 13, 19, 26, 28, 33, 43, 53, 60]] = 1
  new_groups[12, [3, 6, 17, 24, 28, 34, 42, 44, 46, 57]] = 1
  new_groups[13, [0, 1, 5, 20, 28, 35, 36, 54, 66, 68]] = 1
  new_groups[14, [5, 7, 19, 23, 24, 30, 39, 48, 67]] = 1
  new_groups[15, [7, 11, 14, 25, 29, 38, 42, 45, 60, 63]] = 1
  new_groups[16, [14, 15, 18, 19, 21, 36, 46, 47, 51, 59]] = 1
  new_groups[17, [22, 27, 36, 38, 43, 44, 49, 65, 69]] = 1
  new_groups[18, [12, 21, 22, 25, 34, 39, 52, 54, 58, 64]] = 1
  new_groups[19, [0, 2, 9, 32, 37, 42, 47, 58, 65, 67]] = 1
  new_groups[20, [16, 32, 38, 46, 48, 53, 55, 62, 64, 66]] = 1
  new_groups[21, [17, 20, 31, 49, 51, 52, 55, 60]] = 1
  return np.array(new_groups, dtype=bool)

def origami_m2():
  new_groups = onp.zeros((22,231))
  new_groups[0, [9, 17, 23, 32, 69, 71, 73, 79, 87, 107, 116, 126, 134, 138, 146, 171, 187, 190, 205, 209, 230]] = 1
  new_groups[1, [0, 1, 6, 41, 57, 71, 75, 97, 99, 103, 113, 148, 153, 164, 204, 208, 212, 214, 223, 228, 229]] = 1
  new_groups[2, [1, 25, 26, 32, 33, 35, 43, 44, 54, 56, 60, 61, 62, 67, 86, 123, 137, 183, 217, 218, 227]] = 1
  new_groups[3, [8, 11, 16, 23, 26, 38, 63, 77, 90, 99, 108, 142, 149, 175, 177, 181, 195, 198, 200, 210, 226]] = 1
  new_groups[4, [5, 12, 15, 16, 36, 39, 44, 47, 82, 89, 91, 107, 117, 153, 158, 172, 173, 178, 185, 186, 219]] = 1
  new_groups[5, [2, 7, 22, 30, 68, 76, 81, 104, 106, 113, 120, 123, 142, 144, 151, 152, 186, 187, 188, 192, 193]] = 1
  new_groups[6, [6, 18, 27, 28, 47, 84, 86, 96, 100, 108, 109, 133, 135, 159, 162, 167, 171, 176, 179, 188, 196]] = 1
  new_groups[7, [4, 20, 21, 27, 29, 30, 51, 62, 82, 87, 94, 114, 127, 139, 148, 150, 166, 174, 182, 203, 226]] = 1
  new_groups[8, [45, 53, 59, 60, 81, 90, 93, 110, 111, 112, 122, 145, 150, 158, 168, 176, 194, 206, 209, 212, 215]] = 1
  new_groups[9, [9, 13, 14, 22, 61, 84, 91, 103, 129, 143, 149, 161, 180, 189, 194, 201, 202, 203, 211, 216, 222]] = 1
  new_groups[10, [0, 3, 5, 18, 45, 55, 58, 66, 78, 85, 120, 128, 130, 138, 147, 163, 166, 181, 183, 184, 202]] = 1
  new_groups[11, [7, 35, 38, 58, 74, 98, 111, 114, 118, 131, 154, 157, 179, 190, 191, 199, 201, 213, 219, 225, 228]] = 1
  new_groups[12, [8, 14, 39, 49, 52, 56, 66, 70, 74, 76, 80, 95, 105, 110, 116, 119, 136, 139, 156, 164, 167]] = 1
  new_groups[13, [2, 15, 21, 31, 41, 52, 53, 54, 63, 64, 65, 72, 79, 102, 118, 129, 135, 140, 147, 160, 165]] = 1
  new_groups[14, [49, 77, 83, 85, 93, 100, 102, 106, 115, 117, 121, 132, 137, 170, 182, 191, 197, 205, 214, 216, 220]] = 1
  new_groups[15, [25, 28, 34, 40, 50, 55, 57, 73, 80, 89, 121, 122, 127, 141, 155, 165, 177, 189, 192, 207, 225]] = 1
  new_groups[16, [4, 12, 13, 19, 33, 48, 70, 72, 88, 104, 109, 124, 126, 128, 145, 154, 155, 175, 197, 208, 224]] = 1
  new_groups[17, [10, 24, 29, 48, 50, 64, 92, 112, 133, 134, 136, 152, 163, 169, 170, 173, 195, 199, 204, 222, 227]] = 1
  new_groups[18, [3, 20, 46, 65, 83, 97, 101, 125, 131, 151, 156, 169, 172, 196, 200, 206, 207, 211, 218, 224, 230]] = 1
  new_groups[19, [19, 34, 36, 37, 42, 67, 68, 69, 92, 98, 115, 119, 125, 130, 143, 159, 160, 174, 210, 215, 223]] = 1
  new_groups[20, [10, 17, 37, 46, 94, 105, 124, 132, 140, 141, 157, 162, 168, 180, 184, 185, 193, 198, 217, 221, 229]] = 1
  new_groups[21, [11, 24, 31, 40, 42, 43, 51, 59, 75, 78, 88, 95, 96, 101, 144, 146, 161, 178, 213, 220, 221]] = 1
  return np.array(new_groups, dtype=bool)


@gin.configurable
class Origami(group_selector.GroupSelector):
  """Pre-computed group patterns."""

  ORIGAMIS = {
      271: origami_xl5,
      68: origami_l5,
      70: origami_m3,
      231: origami_m2,
      274: origami_l3
  }

  def get_groups(self, rng, state):
    fn = self.ORIGAMIS.get(state.num_patients, None)
    if fn is None:
      raise ValueError(f"No such origami of size {state.num_patients}")
    return fn()

