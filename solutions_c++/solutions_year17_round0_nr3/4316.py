#include <bits/stdc++.h>
#define mod 10000000007
using namespace std;

int main()
{
     freopen ("C:\\Users\\Muhammed\\ClionProjects\\C-small-2-attempt0.in","r",stdin);
     freopen ("C:\\Users\\Muhammed\\ClionProjects\\C-small-2-attempt0.out","w",stdout);
    int tests ;
    cin >> tests;
    int counter;
    counter = 1;
    while(tests--){
        long long n , k;
        cin >> n >> k ;
        long long range = log2(k);
        long long place = n-k;
        long long mappedValue = place/(1<<(range));
        cout << "Case #"<<counter<<": "<< (mappedValue+1)/2 << " " << mappedValue/2 << endl;
        counter++;
    }
}
