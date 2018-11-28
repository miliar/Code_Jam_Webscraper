#include<iostream>
//#include<stack>
using namespace std;
stack<char> s1;
//int count1=0;
int check(string s,int n,int l,int j1){
    int i=0,j,k,temp,temp1=0;
    int count1=0;
    while(i<n){
            //cout<<"!";
            //cout<<"i is "<<i<<endl;
    for(i=0;i<n;i++){
        if(s[i]=='-'){
                if(i>(n-l+1)){
                    cout<<"Case #"<<j1<<":"<<" "<<"IMPOSSIBLE"<<endl;
                    temp1=1;
                    break;
                }
                //cout<<"!";
                //cout<<"i is "<<i<<endl;
            //temp=i;
            j=i;
            while(j<i+l){
                //cout<<"!";
                //cout<<"i is "<<i<<endl;
                if(s[j]=='+'){
                    s[j]='-';
                }
                else{
                    s[j]='+';
                }
                j++;
                //count1++;
            }
            count1++;
        }
    }
    if(temp1==1){
        break;
    }
    }
    //cout<<s;
    if(temp1!=1){
    cout<<"Case #"<<j1<<":"<<" "<<count1<<endl;
    }
    return 0;
}
int main(){
    string s;
    int t;
    cin>>t;
    int j=1;
    while(j<=t){
    //int j,k;
    int l;
    cin>>s;
    cin>>l;
    int n=s.length();
    //cout<<n;
    //while(check(s,n)!=0){
    //cout<<s;
    int temp=check(s,n,l,j);
  //  count1=0;
    j++;
    }
    return 0;
}
