#include<iostream>
#include<stdlib.h>

using namespace std;

int T; //Testcase
long long N; //Maxmum number
int * NArr; //
int l; //length of Number
bool tidy;

void ChangeToArray(){
long long temp = N;

l = 1;
while ((temp/=10) != 0)
l++;

NArr = new int[l];

temp = N;
for (int i = l-1; i > -1 ; i--)
{
NArr[i] = temp%10;
temp /= 10;
}
}

void cal()
{
int idx = 0;
tidy = true;

for (int i = 0; i < l-1; i++)
{
if (NArr[i] > NArr[i+1])
{
idx = i;
tidy = false;
break;
}
}

if (tidy == false)
{
for (int i = idx; i>=0; i--)
{
if (NArr[i] != NArr[i - 1])
{
idx = i;
break;
}
}
NArr[idx] -= 1;

for (int i = idx + 1; i < l; i++)
{
NArr[i] = 9;
}

}

for (int i = 0; i < l; i++){
if (NArr[i] == 0)
continue;
printf("%d", NArr[i]);
}
printf("\n");
}

int main(){
scanf("%d", &T);

for (int i=1; i < T+1;i++)
{
scanf("%lld", &N);
ChangeToArray();
printf("Case #%d: ", i);
cal();
}

return 0;
}