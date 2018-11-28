#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool istidy(int n){
if(n<= 10)return true ;
vector<int> s ;
int smallest = 10,flag = 1 ;
while(n>0){
    int x = n%10 ;
    s.push_back(x) ;
    n = n/10 ;
}
for(int i = 0 ; i< s.size() ; i++){
    for(int j = 0 ; j<i ; j++){
        if(s[j]<s[i]){
            flag = 0 ; break ;
        }
    }
}
if(flag == 1) return true ;
else return false ;
}
int main()
{
    freopen("B-small-attempt4.in","r",stdin);
   freopen("outputsmall.out","w",stdout);
    int tc,j = 1 ;
    cin>>tc ;
    while(tc--){
        int n ;
        cin>>n ;
        cout<<"Case #"<<j<<": " ;
        for(int i = n ; i>0 ; i--){
            if(istidy(i)){
                cout<<i<<endl  ;
                break ;
            }
        }
        j++ ;
    }
    return 0;
}
