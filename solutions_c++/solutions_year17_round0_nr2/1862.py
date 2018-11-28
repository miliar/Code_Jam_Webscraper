#include<bits/stdc++.h>
using namespace std;
int _Max[20];
int _V[20];
int main(){
//	freopen("in","r",stdin);
	int T;
	cin>>T;
	for(int I=1;I<=T;I++){
		string tmp;
		cin>>tmp;
		_Max[0]=0;
		_V[1]=_Max[1]=tmp[0]-'0';
		for(int i=1;i<tmp.size();i++){
			_V[i+1]=tmp[i]-'0';
			_Max[i+1]=max(_Max[i],_V[i+1]);
		}
		int pM=tmp.size()+1;
		for(int i=tmp.size();i>1;i--){
			if(_V[i]>=_Max[i-1])	continue;
			else{
				while(_V[i]-1<_Max[i-1])
					i--;
				_V[i]-=1;
				for(int p=pM+1;p>i;p--)
					_V[p]=9;
				pM=i+1;
			}
		}
		cout<<"Case #"<<I<<": ";
		bool flag=false;
		for(int i=1;i<=tmp.size();i++){
			if(_V[i])	flag=true;
			if(flag||_V[i])
				cout<<_V[i];
		}
		cout<<endl;
	}
}
