#include <iostream>
#include <vector>

bool tria(int a, int b, int c){
	if(a<0||b<0||c<0)
		return false;
	if(a+b<c||a+c<b||b+c<a)
		return true;
	return false;
}

void contest(){
	int n;
	std::cin>>n;
	std::vector<int> colors(6);
	for(int i=0;i<6;++i){
		std::cin>>colors[i];
	}

	bool pairO,pairG,pairV;

	pairO=colors[1]<=colors[4];
	pairG=colors[3]<=colors[0];
	pairV=colors[2]>=colors[5];

	int BO,RG,YV;
	if(!pairO || !pairG || !pairV){
		std::cout<<"IMPOSSIBLE";
		return;
	}

	BO=colors[1];
	colors[4]-=BO;
	colors[1]=0;
	RG=colors[3];
	colors[0]-=RG;
	colors[3]=0;
	YV=colors[5];
	colors[2]-=YV;
	colors[5]=0;
	/*
	int x=BO+RG;
	int y=RG+YV;
	int z=BO+YV;
	if((RG>0&&z>0)||(BO>0&&y>0)||(YV>0&&x>0)){
	}
	*/
	bool fail = false;
	
	if(BO){
		if(BO*2!=n){
			if(colors[4]==0){
				fail = true;
			}
		}else{
			for(int i=0;i<BO;++i){
				std::cout<<"BO";
			}
			return;
		}
	}

	if(RG){
		if(RG*2!=n){
			if(colors[0]==0){
				fail=true;
			}
		}else{
			for(int i=0;i<RG;++i){
				std::cout<<"RG";
			}
			return;
		}
	}

	if(YV){
		if(YV*2!=n){
			if(colors[2]==0){
				fail=true;
			}
		}else{
			for(int i=0;i<YV;++i){
				std::cout<<"YV";
			}
			return;
		}

	}

	if(tria(colors[0],colors[2],colors[4])){
		fail=true;
	}

	if(fail){
		std::cout<<"IMPOSSIBLE";
		return;
	}

	int pos=0;
	int start=0;
	if(colors[2]>colors[0]){
		start=2;
	}

	if(colors[4]>colors[start]){
		start=4;
	}
	int current=start;
	while(pos<n){
		bool placed = false;
		switch(current){
		case 0:
			if(RG){
				--RG;
				std::cout<<"RG";
				pos+=2;
				if(tria(colors[0]-1,colors[2],colors[4])){
					std::cout<<"R";
					--colors[0];
					++pos;
					placed=true;
				}
			}else{
				std::cout<<"R";
				--colors[0];
				++pos;
				placed=true;
			}
			break;
		case 2:
			if(YV){
				--YV;
				std::cout<<"YV";
				pos+=2;
				if(tria(colors[0],colors[2]-1,colors[4])){
					std::cout<<"Y";
					--colors[2];
					++pos;
					placed=true;
				}
			}else{
				std::cout<<"Y";
				--colors[2];
				placed=true;
				++pos;
			}
			break;
		case 4:
			if(BO){
				--BO;
				std::cout<<"BO";
				pos+=2;
				if(tria(colors[0],colors[2],colors[4]-1)){
					std::cout<<"B";
					--colors[2];
					++pos;
					placed=true;
				}
			}else{
				std::cout<<"B";
				--colors[4];
				++pos;
				placed=true;
			}
			break;
		}

		if(placed){
			switch(current){
			case 0:
				if(colors[2]>colors[4]){
					current=2;
				}
				else if(colors[2] == colors[4]){
					if(start == 2){
						current=start;
					}else{
						current = 4;
					}
				}else{
					current = 4;
				}
				break;
			case 2:
				if(colors[0]>colors[4]){
					current=0;
				}else if(colors[0] == colors[4]){
					if(start == 0){
						current=start;
					}else{
						current = 4;
					}
				}
				else{
					current=4;
				}
				break;
			case 4:
				if(colors[0]>colors[2]){
					current=0;
				}
				else if(colors[0] == colors[2]){
					if(start == 0){
						current=start;
					}else{
						current = 2;
					}
				}
				else
					current=2;
				break;
			}
		}
	}
}

int main(){
	int n;
	std::cin>>n;
	++n;
	for(int i=1;i<n;++i){
		std::cout<<"Case #"<<i<<": ";
		contest();
		std::cout<<'\n';
	}

	return 0;
}