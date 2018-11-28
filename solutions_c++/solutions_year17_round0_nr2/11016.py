#include <iostream>
using namespace std;

int main ()
{
int T;

unsigned long long N;

cin >> T;

int i = 0;
unsigned long long d1, d2, d3;
unsigned long long num;
while (i < T)
{

cin >> N;


num = N;
d2 = N;
d3 = 10;
while ( d2 %10 ||d2/10)
{
d1 = d2%10;
d2 /=10;
if (d1 >  d3)
{
d3 = 10;
num--;
d2 = num;
}
else
{
d3 = d1;
}
}

cout << "Case #" << i+1  << ": " << num << endl;


i++;
}


return 0;
}
