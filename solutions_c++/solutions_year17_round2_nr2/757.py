// Template and program by vvneagleone

#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<climits>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
#define MOD 1000000007LL

#ifdef __GNUC__
    #if ( __GNUC__ >= 4 && __GNUC_MINOR__ >= 7 && __cplusplus > 201100L )
        #include<unordered_set>
        #include<unordered_map>
    #endif
#endif // __GNUC__

#ifdef __WIN32
    #define gx getchar
    #define px putchar
    #define ps putchar(' ')
    #define pn putchar('\n')
#else
    #define gx getchar_unlocked
    #define px putchar_unlocked
    #define ps putchar_unlocked(' ')
    #define pn putchar_unlocked('\n')
#endif // __WIN32

void scan(int &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*sign;}
void lscan(LL &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*(LL)(sign);}
int sscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n')a[i++]=c,c=gx();a[i]=0;return i;}
int wscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n'&&c!=' ')a[i++]=c,c=gx();a[i]=0;return i;}
void print(int n){if(n<0){n=-n;px('-');}int i=10;char o[10];do{o[--i]=(n%10)+'0';n/=10;}while(n);do{px(o[i]);}while(++i<10);}
void lprint(LL n){if(n<0LL){n=-n;px('-');}int i=21;char o[21];do{o[--i]=(n%10LL)+'0';n/=10LL;}while(n);do{px(o[i]);}while(++i<21);}
void sprint(const char*a){const char*p=a;while(*p)px(*p++);}
LL power(LL b,LL e,LL m=MOD){LL r=1;while(e){if(e&1)r=(r*b)%m;b=(b*b)%m;e>>=1;}return r;}
LL minvp(LL n, LL m=MOD){return power(n,m-2,m);}
LL minv(LL a,LL m=MOD){LL c,t,q,x,y;c=m;x=0;y=1;while(a>1){q=a/c;t=c;c=a%c;a=t;t=x;x=y-q*x;y=t;}if(y<0)y+=m;return y;}
LL mmul(LL a,LL b,LL m=MOD){LL x=0,y=a%m;while(b){if(b&1)x=(x+y)%m;y=(y<<1)%m;b>>=1;}return x%m;}
LL absll(LL x){if(x<0)return -x;return x;}

LL t, tt, N, R, O, Y, G, B, V, M;
LL i, j, k;

char maxchar, midchar, minchar;
LL maxn, midn, minn;

int main() {
    lscan(tt);
    for( t = 1; t <= tt; ++t ) {
        cout << "Case #" << t << ": ";
        lscan(N);lscan(R);lscan(O);lscan(Y);lscan(G);lscan(B);lscan(V);
        M = N;

        if( O ) {
            if( O > B ) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            if( O == B ) {
                if( R == 0 && Y == 0 && G == 0 && V == 0 ) {
                    while(O--) {
                        cout << "BO";
                    }
                    cout << endl;
                    continue;
                }
                else {
                    cout << "IMPOSSIBLE" << endl;
                    continue;
                }
            }
            else {
                B -= O;
                N -= 2*O;
            }
        }

        if( G ) {
            if( G > R ) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            if( G == R ) {
                if( O == 0 && Y == 0 && B == 0 && V == 0 ) {
                    while(G--) {
                        cout << "RG";
                    }
                    cout << endl;
                    continue;
                }
                else {
                    cout << "IMPOSSIBLE" << endl;
                    continue;
                }
            }
            else {
                R -= G;
                N -= 2*G;
            }
        }

        if( V ) {
            if( V > Y ) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            if( V == Y ) {
                if( R == 0 && O == 0 && G == 0 && B == 0 ) {
                    while(V--) {
                        cout << "YV";
                    }
                    cout << endl;
                    continue;
                }
                else {
                    cout << "IMPOSSIBLE" << endl;
                    continue;
                }
            }
            else {
                Y -= V;
                N -= 2*V;
            }
        }

        // large: only RYB
        if( R >= Y && R >= B ) {
            maxchar = 'R';
            maxn = R;
            if( Y >= B ) {
                midchar = 'Y';
                midn = Y;
                minchar = 'B';
                minn = B;
            }
            else {
                midchar = 'B';
                midn = B;
                minchar = 'Y';
                minn = Y;
            }
        }
        else if( Y >= R && Y >= B ) {
            maxchar = 'Y';
            maxn = Y;
            if( R >= B ) {
                midchar = 'R';
                midn = R;
                minchar = 'B';
                minn = B;
            }
            else {
                midchar = 'B';
                midn = B;
                minchar = 'R';
                minn = R;
            }
        }
        else {
            maxchar = 'B';
            maxn = B;
            if( Y >= R ) {
                midchar = 'Y';
                midn = Y;
                minchar = 'R';
                minn = R;
            }
            else {
                midchar = 'R';
                midn = R;
                minchar = 'Y';
                minn = Y;
            }
        }
        if( maxn > N/2 ) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        char out[1005];
        out[N] = 0;
        LL last;
        for( i = 0; maxn; i += 2 ) {
            out[i] = maxchar;
            last = i+1;
            --maxn;
        }
        for( i = 1; midn > minn; i += 2 ) {
            out[i] = midchar;
            --midn;
        }
        bool alt = 0;
        for( ; i <= last ; i += 2 ) {
            if(alt) {
                out[i] = minchar;
                --minn;
                alt = 0;
            }
            else {
                out[i] = midchar;
                --midn;
                alt = 1;
            }
        }
        for( i = last+1; i < N; ++i ) {
            if(alt) {
                out[i] = minchar;
                --minn;
                alt = 0;
            }
            else {
                out[i] = midchar;
                --midn;
                alt = 1;
            }
        }

        for( i = 0; i < N; ++i ) {
            if( out[i] == 'R' ) {
                if( G > 0 ) {
                    while(G--) {
                        cout << "RG";
                    }
                }
                cout << "R";
            }
            if( out[i] == 'Y' ) {
                if( V > 0 ) {
                    while(V--) {
                        cout << "YV";
                    }
                }
                cout << "Y";
            }
            if( out[i] == 'B' ) {
                if( O > 0 ) {
                    while(O--) {
                        cout << "BO";
                    }
                }
                cout << "B";
            }
        }
        cout << endl;
    }
    return 0;
}
