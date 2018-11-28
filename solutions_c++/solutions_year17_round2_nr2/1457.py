#include <iostream>
using namespace std;
typedef long long ll;

int T,n,c[7];

bool ok(int a,int b){
    if(a == 6){
        return true;
    }
    if((a+1)%6 == b){
        return false;
    }
    if(a%6 == b){
        return false;
    }
    if((a+5)%6 == b){
        return false;
    }
    return true;
}

int main()
{
    freopen("input3.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int q = 1;q<=T;q++){
        cin>>n>>c[0]>>c[1]>>c[2]>>c[3]>>c[4]>>c[5];
        if((n/2<c[0])||(n/2<c[1])||(n/2<c[2])||(n/2<c[3])||(n/2<c[4])||(n/2<c[5])){
            printf("Case #%d: IMPOSSIBLE\n",q);
        }
        else{
            printf("Case #%d: ",q);
            int arrays[1005] = {};
            int prev = 6;
            for(int i = 0;i<n;i++){
                int tmp = 0;
                int index;
                for(int j = 0;j<6;j++){
                    if(ok(prev,j)&&tmp<c[j]){
                        tmp = c[j];
                        index = j;
                    }
                }
                arrays[i] = index;
                c[index]--;
                //printf("%d : c[%d]\n",c[index],index);
                prev = index;
            }
            if(arrays[n-1] == arrays[0]){
                swap(arrays[n-1],arrays[n-2]);
            }
            for(int i = 0;i<n;i++){
                if(arrays[i] == 0){
                    printf("R");
                }
                else if(arrays[i] == 1){
                    printf("O");
                }
                else if(arrays[i] == 2){
                    printf("Y");
                }
                else if(arrays[i] == 3){
                    printf("G");
                }
                else if(arrays[i] == 4){
                    printf("B");
                }
                else if(arrays[i] == 5){
                    printf("V");
                }
            }
            printf("\n");
        }
    }
}
