#include<iostream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

int main() {

	int T;
	cin>>T;
	cin.clear();

	for(int i=1;i<=T;i++) {
		string S;
		cin>>S;
		//cout<<S<<":"<<endl;
		int K;
		cin>>K; cin.clear();

		int slen=S.length();
		int sizeD=pow(2,slen);
		//cout<<sizeD<<":"<<endl;;
		vector<int> d = vector<int>(sizeD,-1);
		d[sizeD-1]=0;

		int mask=(1<<K) -1;
		//cout<<mask<<":mask"<<endl;
		for(int j=sizeD-1;j>=0;j--) {
			if(d[j]!=-1) {
				for(int l=0;l<=slen-K;l++) {
					int x = j^(mask<<l);
					if(d[x]==-1 || d[x]>d[j]+1)
						d[x]=d[j]+1;
				}
			}
		}
		int x=0;
		for(string::iterator it=S.begin();it!=S.end();it++) {
			if((*it)=='+') {
				x+=pow(2,slen-1);
			}
			slen--;
		}
		if(d[x]>-1)
		cout<<"Case #"<<i<<": "<<d[x]<<endl;
		else
		cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
	}
}