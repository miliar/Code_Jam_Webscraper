#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);

    int t,p=1;
    cin>>t;
    while(t--){
        long long int n,k,maxs,mins,loc;
        cin>>n>>k;
        long long int arr[n][3];
        for(long long int i=0;i<n;i++){
            arr[i][0]=0;
            arr[i][1]=i;
            arr[i][2]=n-i-1;
        }
        for(long long int j=0;j<k;j++){
            for(long long int i=0;i<n;i++){
                if(arr[i][0]!=1){
                    maxs=min(arr[i][1],arr[i][2]);
                    loc=i;
                    break;
                }
            }
            for(long long int i=loc+1;i<n;i++){
                if((arr[i][0]!=1)&&(maxs<(min(arr[i][1],arr[i][2])))){
                    maxs=min(arr[i][1],arr[i][2]);
                    loc=i;
                }
            }
            long long int l=arr[loc][1],r=arr[loc][2];
            if(l<r){
                for(long long int i=loc+1;i<n;i++){
                    if(arr[i][0]!=1&&arr[i][1]==l&&arr[i][2]>r){
                        r=arr[i][2];
                        loc=i;
                    }
                }
            }
            else if(l>r){
                for(long long int i=loc+1;i<n;i++){
                    if(arr[i][0]!=1&&arr[i][2]==r&&arr[i][1]>l){
                        l=arr[i][1];
                        loc=i;
                    }
                }
            }
            else{
                long long int temploc1=loc,temploc2=loc;
                for(long long int i=loc+1;i<n;i++){
                    if(arr[i][0]!=1&&arr[i][1]==l&&arr[i][2]>r){
                        r=arr[i][2];
                        temploc1=i;
                    }
                }
                for(long long int i=loc+1;i<n;i++){
                    if(arr[i][0]!=1&&arr[i][2]==r&&arr[i][1]>l){
                        l=arr[i][1];
                        temploc2=i;
                    }
                }
                if((arr[temploc1][1]+arr[temploc1][2])>(arr[temploc2][1]+arr[temploc2][2]))
                    loc=temploc1;
                else
                    loc=temploc2;
            }
            arr[loc][0]=1;
            long long int x=loc-1,a=0;
            while(arr[x][0]!=1&&x>=0){
                arr[x--][2]=a++;
            }
            x=loc+1,a=0;
            while(arr[x][0]!=1&&x<n){
                arr[x++][1]=a++;
            }
        }
        maxs=max(arr[loc][1],arr[loc][2]);
        mins=min(arr[loc][1],arr[loc][2]);
        cout<<"Case #"<<p++<<": "<<maxs<<" "<<mins<<endl;
    }

    return 0;
}
