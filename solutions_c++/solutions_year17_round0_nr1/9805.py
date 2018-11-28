#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <cstring>
using namespace std;


bool isstringofone(string str){
bool flag = 1 ;
for(int i = 0 ; i< str.length() ; i++){
    if(str[i] != '1'){
        flag = 0 ; break ;
    }
}
if(flag == 1) return true ;
else return false ;
}

int flip(string str,int j,int ans,int k){
if(isstringofone(str)) return ans ;
if(j == str.length()-1){
    if(!isstringofone(str)) return 10000000 ;
    return ans ;
}

string str1 = str ;
if(j< str.length()-k+1){
for(int i = 0 ;i< k;i++){
 if(str1[j+i] == '0')str1[j+i] = '1' ;
 else str1[j+i] = '0' ;
 }
}
//cout<<str1<<" "<<str<<endl ;
int ans1 = flip(str,j+1,ans,k) ;
int ans2 = flip(str1,j+1,ans+1,k) ;

return min(ans1,ans2) ;

}

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
   freopen("outputsmall.out","w",stdout);
    int tc ;
    cin>>tc ;
    int j = 1 ;
    while(tc--){
    string str ;
    int k ;
    cin>>str>>k ;
    for(int i = 0 ; i< str.length() ; i++){
        if(str[i] == '+') str[i] = '1' ;
        else str[i] = '0' ;
    }
    int ans  = flip(str,0,0,k) ;
    cout<<"Case #"<<j<<": " ;
    if(ans == 10000000) cout<<"IMPOSSIBLE"<<endl ;
    else
    cout<<ans<<endl ;
    j++ ;
    }
   return 0 ;
}
