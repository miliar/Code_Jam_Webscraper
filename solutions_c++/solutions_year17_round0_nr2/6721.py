#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
int main()
{
int N;
scanf("%d", &N);
char ch[10000];
int k;
for(int I=1; I<=N; ++I)
{
scanf("%s", ch);
int len = strlen(ch);
if(len == 1)
{
printf("Case #%d: %s\n", I, ch);
continue;
}

for(;;)
{
int start = 0;
//if(ch[start]=='0') ++start;
//assert(ch[start]!='0');
while(start+1<len && ch[start]<=ch[start+1]) ++start;
if(start+1 == len)
{
if(ch[0]=='0')
{
assert(ch[1]!='0');
	printf("Case #%d: %s\n", I, ch+1);
}
else
	printf("Case #%d: %s\n", I, ch);
break;
}
//if(ch[start]=='0' && start==0)
//  assert(false);
while(ch[start]=='0' && start>=0) --start;
//printf("start1=%d %d\n", start, len);
assert(start>=0);
if(start>0)
{
	while(ch[start]==ch[start-1] && start>0) --start;
	//--start;
	//printf("start2=%d\n", start);
}
assert(ch[start]>'0');
assert(start>=0);
ch[start]--;
//printf("start3=%s\n", ch);
for(int i=start+1; i<len; ++i)
  ch[i]='9';
//printf("start4=%s\n", ch);
//continue;
//break;

} // end for

}

return 0;
}