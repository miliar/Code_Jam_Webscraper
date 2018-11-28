#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
        int n,m;
        cin>>n>>m;
        string a[100];
        cerr<<n<<" "<<m<<endl;
        for (int i=0;i<n;i++) cin>>a[i];

        for (int i=0;i<n;i++){
            bool isempty=true;
            for (int j=0;j<m;j++) if (a[i][j]!='?') isempty=false;

            if (!isempty){
                    while(1){
                        int idx=-1;
                        for (int j=0;j<m;j++) if (a[i][j]=='?') {idx=j;break;}
                        if (idx==-1) break;
                        int tmp=idx;
                        while (tmp>=0&&a[i][tmp]=='?') tmp--;
                        if (tmp>=0) a[i][idx]=a[i][tmp];else{
                            tmp=idx;
                            while(tmp<m&&a[i][tmp]=='?') tmp++;
                            a[i][idx]=a[i][tmp];
                        }
                    }
            }

        }

        for (int i=0;i<n;i++)
            if (a[i][0]=='?'){
                int ass=0;
                for (int j=i;j>=0;j--)  if (a[j][0]!='?') {a[i]=a[j];break;ass=1;}
                if (!ass) for (int j=i+1;j<n;j++) if (a[j][0]!='?') {a[i]=a[j];break;}

            }
		cout<<"Case #"<<t<<": "<<endl;
		cerr<<t<<endl;
		for (int i=0;i<n;i++) cout<<a[i]<<endl;
	}
}
