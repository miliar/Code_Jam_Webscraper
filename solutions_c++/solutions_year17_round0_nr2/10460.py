#include <bits/stdc++.h>
using namespace std;
bool areSorted(int n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}
int main()
{
  int t; int m = 0;
  cin>>t;
  while(t-- && ++m){
    int n,i;
    cin>>n;
    int ctr = 0;
    if(n<10)
        cout<<"Case #"<<m<<": "<<n<<endl;
    else
    while(1){
        if(areSorted(n)){
            cout<<"Case #"<<m<<": "<<n<<endl;
            break;
        }
        else
            n--;
    }

  }
    return 0;
}
