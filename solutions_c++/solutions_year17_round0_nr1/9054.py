#include<iostream>
#include<string>
#include<algorithm>
#include<cstring>

using namespace std;

int main() {
int flips = 0,cons=0,q=0;
std::string sign;
int i;
int cases = 0;
cin >> cases;
int foo;
for(foo=1; foo<=cases; foo++)
{
flips = 0;
q = 0;
cin >> sign;
int signlen = sign.size();
cin >> cons;
for(i=signlen; i>0; i--)
{
if(sign[i-1] == '-'){
    if (cons<=i)
    {
flips += 1;
for (int z=1; z<=cons;z++)
{
    if(sign[i-z] == '-')
    {
        sign[i-z] = '+';
    }
    else
    {
        sign[i-z] = '-';
    }
}
}
else 
{
 q=1;
 break;
}
}
}
if(q!=1)
{
cout << "Case #" << foo << ": " << flips << endl;
}
else
{
    cout << "Case #" << foo << ": IMPOSSIBLE" << endl;
}
}
}
