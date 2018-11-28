#include<bits/stdc++.h>
using namespace std;
bool compare(vector<int> &a, vector<int> &b){
    if(a[0]>b[0])
    return 1;
    else if(a[0]<b[0])
    return 0;
    else if(a[1]>b[1])
    return 1;
    else if(a[1]<b[1])
    return 0;
    else
    return a[2]<b[2];
}
int main(){
    freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        int n;
        cin>>n;
        vector<bool> v(n+2,0);
        v[0]=v[n+1]=1;
        int k;
        cin>>k;
        vector<vector<int> > a;
        vector<int> b;
        int ls,rs;
        for(int i=1; i<=k; i++){
            a.clear();
            for(int j=1; j<=n; j++){
                if(v[j])
                continue;
                b.clear();
                ls=rs=0;
                for(int k=j-1; k>0 && v[k]==0; k--)
                ls++;
                for(int k=j+1; k<=n && v[k]==0; k++)
                rs++;
                b.push_back(min(ls,rs));
                b.push_back(max(ls,rs));
                b.push_back(j);
                a.push_back(b);
            }

            sort(a.begin(),a.end(),compare);
            //for(int i=0; i<a.size(); i++)
            //cout<<a[i][0]<<" "<<a[i][1]<<" "<<a[i][2]<<"\n";
            v[a[0][2]]=1;
            //for(int i=0; i<v.size(); i++)
            //cout<<v[i]<<" ";
            //cout<<endl;
        }
        printf("Case #%d: %d %d\n",t,a[0][1],a[0][0]);
	}
	return 0;
}
