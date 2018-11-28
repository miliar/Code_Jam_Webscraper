#include<fstream>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int main() {
	freopen("C-small-1-attempt3.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	unsigned long int n,k;
	for(int i=1;i<=t;i++){
		cin>>n>>k;
		bool* ar=new bool[n+2];
		for(int j=1;j<=n;j++)
			ar[j]=0;
		ar[0]=ar[n+1]=1;
		//k-=1;
		//int maxx,minn;
		int minmax,maxmax,ls,rs;
		int pos;
		while(k--){
			//int pos=maximal(ar);
			minmax=-1,maxmax=-1;
			//int pos;
			int count_min=0,count_max=0,pos_min,pos_max;
			for(int j=1;j<=n;j++){
				if(ar[j]==0){
					int k=j-1;
					while(ar[k]==0 && k>=0)
						k--;
					ls=j-k-1;
					
					k=j+1;
					while(ar[k]==0 && k<=n+1)
						k++;
					rs=k-j-1;
					
					int _min=(ls<rs)?ls:rs;
					int _max=(ls>rs)?ls:rs;
					if(_min>minmax){
						minmax=_min;
						count_min=0;
						pos_min=j;
						
						maxmax=_max;
						count_max=0;
						pos_max=j;
						//cout<<minmax<<" ";
					}
					else if(_min==minmax){
						count_min++;
						if(_max>maxmax){
							maxmax=_max;
							count_max=0;
							pos_max=j;
							//cout<<maxmax<" ";
						}
						else if(_max==maxmax)
							count_max++;
					}
					//cout<<endl;
					
				}
			}
			//int pos;
			if(count_min==0)
				pos=pos_min;
			else if(count_max==0)
				pos=pos_max;
			else 
				pos=pos_max;
			//cout<<pos<<endl;
			ar[pos]=1;
			/*for(int j=0;j<=n+1;j++)
				cout<<ar[j]<<" ";
			cout<<endl;*/
		}
			int k=pos-1;
			while(ar[k]==0 && k>=0)
				k--;
			ls=pos-k-1;
					
			k=pos+1;
			while(ar[k]==0 && k<=n+1)
				k++;
			rs=k-pos-1;
			
			cout<<"Case #"<<i<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
	}
	return 0;
}
