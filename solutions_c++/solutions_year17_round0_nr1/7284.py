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
int getBoolArray(bool* buffer){
    int length = 0;
    for (char c=gc; c=='+'||c=='-'; c = gc,length++)buffer[length]=(c=='+');
    return length;
}
void flipAt(bool *buffer, int at, int flipLength){
    while(flipLength--)buffer[at]=!buffer[at++];
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
int main()
{
    unsigned int t,i,testCaseNo=0,length,k,totalFlips;
    s(t);
    bool buffer[1001], isImpossible;
    while(testCaseNo++<t){
        length=getBoolArray(buffer);
        s(k);
        isImpossible=false;
        totalFlips=0;
        for(i=0;i<=length-k;i++){
            if(!buffer[i]){
                flipAt(buffer,i,k);
                totalFlips++;
            }
        }
        for(;i<length;i++){
            if(!buffer[i]){
                isImpossible=true;
                break;
            }
        }
        codeJamOutput(testCaseNo);
        if(isImpossible){
            printf("IMPOSSIBLE\n");
        }
        else{
            w(totalFlips);
        }
    }
    return 0;
}
