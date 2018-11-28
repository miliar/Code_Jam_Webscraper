#include<math.h>
#include<algorithm>
#include <stdio.h>
#define gc getchar()
#define pc(ch) putchar(ch)
using namespace std;
inline void s(unsigned long long &x) {
    register int c = gc;
     x = 0;
    bool neg = false;
    for (; ((c < 48 || c > 57) && c != '-'); c = gc);
    if (c == '-') {
    	neg = true;
    	c = gc;}
    for (; c > 47 && c < 58; c = gc) {
    	x = (x << 1) + (x << 3) + c - 48;
    }
    if (neg) {
    	x = -x;
    }
}
inline void w(unsigned long long n, bool endLine=true) {
	unsigned long long N = n, rev, count = 0;
    rev = N;
    if (! N) {
    	pc('0');
    	pc('\n');
    	return;
    }
    while (! (rev % 10)) {
    	count++;
    	rev /= 10;
    }
    rev = 0;
    while (N) {
    	rev = (rev << 3) + (rev << 1) + N % 10;
    	N /= 10;
    }
    while (rev) {
    	pc(rev % 10 + '0');
    	rev /= 10;
    }
    while (count--) {
    	pc('0');
    }
    if(endLine)pc('\n');
}
inline void s(unsigned int &x)
{
    unsigned long long a;
    s(a);
    x=a;
}
inline unsigned long long pow(int a)
{
    unsigned long long b=1;
    for(int i=0;i<a;i++)b*=a;
    return b;
}
inline void codeJamOutput(int testCaseNo){
    pc('C');
    pc('a');
    pc('s');
    pc('e');
    pc(' ');
    pc('#');
    w(testCaseNo, false);
    pc(':');
    pc(' ');

}
char buffer[20], digits;
inline char* readNoAsString(){
    // read no. till an enter
    digits = 0;
    for (char c=gc; c >= '0' && c <= '9'; c = gc) {
    	buffer[digits++]=c;
    }
    return buffer;
}
void decrementAt(char *buffer, int index){
    if(index==-1)return;
    if(buffer[index]!='0'){
        buffer[index]--;
        return;
    }
    decrementAt(buffer, index-1);
    buffer[index]='9';
}
void handleNonDecreasingSequenceAt(char *n, int index){
    decrementAt(n, index-1);
    if(index>1&&n[index-1]<n[index-2]){
        handleNonDecreasingSequenceAt(n,index-1);
        return;
    }
    for(;index<digits;index++){
        n[index]='9';
    }
}
int main()
{
    unsigned int t,i,testCaseNo=0;
    char *n;
    s(t);
    bool isInNonDecreasingOrder;
    while(testCaseNo++<t){
        n=readNoAsString();
        isInNonDecreasingOrder=true;
        for(i=1;i<digits;i++){
            if(n[i]<n[i-1]){
                handleNonDecreasingSequenceAt(n,i);
                break;
            }
        }
        codeJamOutput(testCaseNo);
        for(i=0;i<digits&&n[i]=='0';i++);
        for(;i<digits;i++)pc(n[i]);
        pc('\n');
    }
    return 0;
}
