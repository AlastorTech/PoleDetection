3
h+�[W  �               @   s   d dl Z dd� Zdd� ZdS )�    Nc             C   s2   t jd�}| d |d< | d |d< | d |d< |S )	N�   r   �   �   �   )r   r   )r   r   )r   r   )�numpy�identity)Zdisplacement�t� r	   �L/Users/liuknan/Documents/GitHub/DetectUtilityPoles/3DModel/transformation.py�translation   s
    
r   c             C   s:   t jd�}| d |d< | d |d< | d |d< d|d	< |S )
Nr   r   r   r   r   )r   r   )r   r   )r   r   )r   r   )r   r   )�scale�sr	   r	   r
   �scaling   s    
r   )r   r   r   r	   r	   r	   r
   �<module>   s   