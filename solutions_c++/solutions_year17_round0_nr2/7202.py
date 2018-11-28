#include <iostream>
#include <string.h>
#include<bits/stdc++.h>
using namespace std;
FILE *in=freopen("inx.in","r",stdin);
FILE *out=freopen("out.txt","w",stdout);
int main(){
	int t,t2;
	cin>>t;
	t2=t;

	int len;
	string n;

	while(t>0){
		cin>>n;
		len=n.length();

		for(int i=0; i<(len-1); i++){
			if(n[i]>n[i+1]){
				n[i]=n[i]-1;
				for(int j=i+1; j<len; j++){
					n[j]='9';
				}
				i=-1;
			}

		}

		if(n[0]!='0')
            cout<<"Case #"<<t2-t+1<<": "<<n<<endl;
        else{
            cout<<"Case #"<<t2-t+1<<": ";
            for(int i=1; i<len; i++)
                cout<<n[i];
            cout<<endl;
        }
		t--;
	}

	return 0;
}
