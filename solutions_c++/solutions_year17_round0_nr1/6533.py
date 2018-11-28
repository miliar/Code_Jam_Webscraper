#include<iostream>
using namespace std;

void flip(string *s, int i, int k) {
	for(int j=i;j<i+k;j++) {
		if ((*s)[j]=='-') (*s)[j]='+';
		else (*s)[j]='-';
	}
}

int main() {
    int T,K,N,i,j,ans;
    string S;
    cin>>T;
    for (j=1;j<=T;j++) {
        cin>>S>>K;
	N=S.size();
	ans=0;
	for (i=0; i<=N-K; i++) {
            if (S[i]=='-') {
		    flip(&S,i,K);
		    ans++;
		    //cout<<S<<endl;
	    }
	}
	bool flag = true;
	for(i=N-K+1;i<N; i++) 
		if(S[i]=='-') {
			flag=false;
			break;
		}
	cout<<"Case #"<<j<<": ";
	if (flag) cout<<ans;
	else cout<<"IMPOSSIBLE";
	cout<<endl;
	//cout<<S<<" "<<S.size()<<endl;
    }
    return 0;
}
