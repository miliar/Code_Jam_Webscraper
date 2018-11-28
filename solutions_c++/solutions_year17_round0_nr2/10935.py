#include<bits/stdc++.h>
using namespace std;

bool check_number(int x){
int digit=x%10;
int nextdigit;
x=x/10;
while(x!=0){
    nextdigit=x%10;
    if(digit<nextdigit)
        return false;
    digit=nextdigit;
    x=x/10;

}

    return true;
}

int main(){
freopen("B-small-attempt1.in", "r", stdin);
freopen("output1.txt", "w", stdout);
int t, x=0, y=0;
cin>>t;
int input[t];
for(int i=0; i<t; i++)
{
    cin>>input[i];
}
for(int i=0; i<t; i++)
{
    bool output=false;
    x=input[i];
    while(output==false)
    {
    output=check_number(x--);
    if(output==true)
        cout<<"Case #"<<i+1<<": "<<x+1<<"\n";
    }
}

}
