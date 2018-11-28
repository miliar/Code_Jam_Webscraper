#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> arr[55];

int i,j,t,test,m,n,a,b,mn,it[55],c;
int k[55];

int main(){
    scanf("%d",&test);
    for(t=1;t<=test;t++){
        scanf("%d %d",&m,&n);
        for(i=0;i<m;i++){
            scanf("%d",&k[i]);
        }
        for(i=0;i<m;i++)arr[i].clear();
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                scanf("%d",&a);
                arr[i].push_back(a);
            }
            sort(arr[i].begin(),arr[i].end());
        }
        for(i=0;i<m;i++)it[i]=0;
        c=0;
        while(1){
            mn=1;
            for(i=0;i<m;i++){
                if(it[i]>=arr[i].size())break;
                a=10*arr[i][it[i]];
                b=k[i]*11;
                a=(a+b-1)/b;
                if(a>mn)mn=a;
            }
            if(i!=m)break;
            for(i=0;i<m;i++){
                if(mn*k[i]*9>10*arr[i][it[i]])break;
            }
            if(i!=m)it[i]++;
            else{
                c++;
                for(i=0;i<m;i++)it[i]++;
            }
        }
        printf("Case #%d: %d\n",t,c);
    }
}
