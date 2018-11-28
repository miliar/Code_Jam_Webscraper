#include <iostream>
#include <string.h>
#include<stdio.h>
using namespace std;
long long maxa,mina;
void get_ans(long long n,long long k)
{
    //cout<<n<<" "<<k<<endl;
    if(n==k)
    {
        maxa = mina = 0;
        return ;
    }
    if(k==1)
    {
        maxa = n/2;
        mina = (n-1)/2;
        return ;
    }
    if(k%2==0)
        get_ans(n/2,k/2);
    else
        get_ans((n-1)/2,k/2);
}
int main() {
  int t;
  freopen("a.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  long long n,k;
  cin >> t;
  for (int i = 1; i <= t; ++i) {

    cin >> n>>k ;
    maxa=mina=-1;
    get_ans(n,k);
    cout << "Case #" << i << ": " <<maxa<<" "<<mina<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
