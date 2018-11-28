#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream input;
    input.open("B-large.in");
    int t;
    input>>t;
    ofstream output;
    output.open("ans_large.txt");
    int casen = 1;
    while(t--)
    {
        long long int n;
        long long int ans;
        input>>n;
        int last = -1;
        long long int n1 = n/10;
        int last_digit = n%10;
        int i = 1;
        bool flag = false;
        while(n1 > 0)
        {
            int x = n1%10;
            if(x > last_digit)
            {
                last = i;
                flag = true;
            }
            else if(x == last_digit && flag == true)
            {
                last = i;
            }
            else
                flag = false;
            last_digit = x;
            n1 /= 10;
            i++;
        }
        if(last == -1)
        {
            ans  = n;
        }
        else
        {
            ans = n;
            int j = 0;
            long long int k = 1;
            while(j < last)
            {
                ans -= k*(n%10);
                j++;
                k *= 10;
                n = n/10;
            }
            ans -= 1;
        }
        output<<"Case #"<<casen<<": ";
        output<<ans<<endl;
        casen++;
    }
}
