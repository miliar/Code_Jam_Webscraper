#include <iostream>
using namespace std;
int T,n;

bool chk(int k){
    int tmp = k%10;
    while(k){
        if(k%10>tmp){
            return false;
        }
        tmp = k%10;
        k/=10;
    }
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int q = 1;q<=T;q++){
        cin>>n;
        for(int i = n;i>0;i--){
            if(chk(i)){
                printf("Case #%d: %d\n",q,i);
                break;
            }
        }
    }
}
