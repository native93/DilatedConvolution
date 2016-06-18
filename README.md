- Main file to run
	- python solve.py

- To initialize from pretrained model
	
	- Download Pretrained model
		sh pretrained/download_kitti.sh

        - Uncomment the following line in solve.py
	    "solver.net.copy_from(weights)"
