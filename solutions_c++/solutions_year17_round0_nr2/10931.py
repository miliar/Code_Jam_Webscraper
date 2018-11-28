#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
bool aresorted(long long int n)
{   if(n/10==0){return true;}
    int next_digit=n%10;
    n=n/10;
    while(n)
    {
        int digit =n%10;
        if(digit <= next_digit){

        next_digit=digit;
        n=n/10;}

        else{break;}
    }
    if(n>0){return false;}
    else if(n==0){return true;}
}


int main(){
    ifstream in("B-small-attempt0.in");
int t;
cin >>t;


for(int k=1;k<t+1;k++)
{
      long long int n;
      cin >> n;
      int temp;
      for(int i=1;i<=n;i++)
      {
        if(aresorted(i)){temp=i;}
      }
 ofstream out("B-small-attempt0.out");
 cout << "Case #"<<k<<": "<<temp<<endl;

}





return 0;}
