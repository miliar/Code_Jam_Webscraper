#include<iostream>
#include<math.h>
#include<algorithm>
#include <stdio.h>
#include <queue>
#include <vector>
#include <utility>
#define ull unsigned long long
#define gc getchar()
#define pc(ch) putchar(ch)
using namespace std;

inline void s(ull &x) {
    register int c = gc;
     x = 0;
    bool neg = false;
    for (; ((c < 48 || c > 57) && c != '-'); c = gc);
    if (c == '-') {
    	neg = true;
    	c = gc;
    }
    for (; c > 47 && c < 58; c = gc) {
    	x = (x << 1) + (x << 3) + c - 48;
    }
    if (neg) {
    	x = -x;
    }
}
inline void w(ull n, bool endLine=true) {
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
    ull a;
    s(a);
    x=a;
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
class Compare{
    public:
     bool operator()(pair<ull,ull> &lhs,pair<ull,ull> &rhs){
        return lhs.first < rhs.first;
    }
};
typedef priority_queue<pair<ull,ull>, vector< pair<ull,ull> >,greater<pair<ull,ull> > > custom_queue;


void breakAndPushIntoQueue(custom_queue &q, pair<ull,ull> &sizeAndCount){
printf("f %llu %llu",sizeAndCount.first,sizeAndCount.second);
    if(sizeAndCount.first&1){
        q.push(make_pair(sizeAndCount.first/2,sizeAndCount.second*2));
        return;
    }
    q.push(make_pair(sizeAndCount.first/2,sizeAndCount.second));
    q.push(make_pair( (sizeAndCount.first-1)/2,sizeAndCount.second) );
    return;
}
pair<ull,ull> pop(custom_queue &q){
    pair<ull,ull> p1=q.top();
    q.pop();
    pair<ull,ull> p2=q.top();
    while(p2.first==p1.first){
        q.pop();
        p1.second+=p2.second;
        p2=q.top();
    }
    return p1;
}
int main()
{
    unsigned int t,testCaseNo=0;
    ull d,initial,speed,n,i;
    long double max_time,time;
    s(t);
    while(testCaseNo++<t){
        s(d);
        s(n);
        max_time=0;
        for(i=0;i<n;i++){
            s(initial);
            s(speed);
            time=(d-initial)/((long double)speed);
            if(time>max_time)max_time=time;
        }
        codeJamOutput(testCaseNo);
        printf("%.6Lf\n",d/max_time);
    }
    return 0;
}
