#include <iostream>

using namespace std;

long long int f(long long n,long long k)
{
    long long int p = 1;
    while(2*p <=k)
    {
        p = p*2;
    }
    return (n-k)/p;
}
int main()
{
    int t;
    cin >> t;

    for(int casenum = 1;casenum<=t;casenum++)
    {
        long long int n;
        long long int k;
        cin >> n >> k;
        long long int answer_sum = f(n,k);
        long long int answer1 = (answer_sum / 2) + answer_sum%2;
        long long int answer2 = (answer_sum / 2);
        cout << "Case #" << casenum << ": " << answer1 << " " << answer2 << endl;
    }
}

