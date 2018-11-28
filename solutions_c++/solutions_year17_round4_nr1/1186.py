#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <queue>
long long t,res,n,c,p;
int cho[5];
using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin>>t;
	for(int test_nr=1;test_nr<=t;test_nr++){
		std::cin>>n>>p;
		for(int i=0;i<5;i++){
			cho[i]=0;
		}
		
		for(int i=0;i<n;i++){
			std::cin>>c;
			cho[c%p]++;
		}
		int res=cho[0];
		if(p==2)
			res+=(cho[1]+1)/2;
		if(p==3){
			int il=min(cho[1],cho[2]);
			cho[1]-=il;
			cho[2]-=il;
			res+=il;
			res+=(cho[1]+2)/3;
			res+=(cho[2]+2)/3;
		}
		if(p==4){
			int il=min(cho[3],cho[1]);
			cho[3]-=il;
			cho[1]-=il;
			cho[2]+=cho[3]/2;
			cho[3]-=(cho[3]/2)*2;
			cho[2]+=cho[1]/2;
			cho[1]-=(cho[1]/2)*2;
			res+=il;
			res+=cho[2]/2;
			cho[2]-=(cho[2]/2)*2;
			if(cho[2]+cho[1]+cho[3]>0)
				res++;
			
		}
		
		std::cout<<"Case #"<<test_nr<<": "<<res<<std::endl;
		
		
	}
}
