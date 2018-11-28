#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
int N;
scanf("%d", &N);
char ch[10000];
int k;
for(int I=1; I<=N; ++I)
{
scanf("%s%d", ch, &k);
int d = 0;
int len = strlen(ch);
for(int i=0; i+k<=len; ++i)
{
if(ch[i]=='-')
{
++d;
for(int j=0; j<k; ++j) { if(ch[i+j]=='+') ch[i+j]='-'; else ch[i+j]='+'; }
} // end if -
//printf("%s\n", ch);
} // end for i
bool done = true;
for(int i=0; i<len; ++i) { if(ch[i]=='-') { done= false; break; } }
if(done)
printf("Case #%d: %d\n", I, d);
else
printf("Case #%d: IMPOSSIBLE\n", I);
} // end for I
return 0;
}