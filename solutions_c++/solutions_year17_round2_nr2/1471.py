#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int main(){
	string fileName="B-small-attempt0";
	freopen((fileName+".in").c_str(),"r",stdin);
	freopen((fileName+".out").c_str(),"w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	char def[7]={"ROYGBV"};
	while(ii<nn){
		cout<<"Case #"<<ii+1<<": ";
			int n;
			int a[6],maxa=-1,maxi,sec,thi;
			cin>>n;
			for(int i=0;i<6;i++){
				cin>>a[i];
				if(a[i]>maxa){
					maxa=a[i];
					maxi=i;
				}
			}
			if(maxi==0){
				sec=2;
				thi=4;
			}
			else if(maxi==2){
				sec=0;
				thi=4;
			}
			else{
				sec=0;
				thi=2;
			}
//			cout<<maxi<<' '<<sec<<' '<<thi<<endl;
			if(maxa>n/2)cout<<"IMPOSSIBLE"<<endl;
			else{
				for(int i=0;i<maxa;i++){
					cout<<def[maxi];
					if(a[sec]>i)cout<<def[sec];
					if(i+a[thi]>=maxa)cout<<def[thi];
				}
				cout<<endl;
			}

		ii++;
	}
}



