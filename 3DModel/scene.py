3
�)�[�  �               @   s   G d d� de �ZdS )c               @   s(   e Zd ZdZdd� Zdd� Zdd� ZdS )	�Sceneg      .@c             C   s   t � | _d S )N)�list�	node_list)�self� r   �C/Users/liuknan/Documents/GitHub/DetectUtilityPoles/3DModel/scene.py�__init__   s    zScene.__init__c             C   s   | j j|� dS )u#    在场景中加入一个新节点 N)r   �append)r   �noder   r   r   �add_node
   s    zScene.add_nodec             C   s   x| j D ]}|j�  qW dS )u&    遍历场景下所有节点并渲染 N)r   �render)r   r	   r   r   r   r      s    zScene.renderN)�__name__�
__module__�__qualname__ZPLACE_DEPTHr   r
   r   r   r   r   r   r      s   r   N)�objectr   r   r   r   r   �<module>   s    