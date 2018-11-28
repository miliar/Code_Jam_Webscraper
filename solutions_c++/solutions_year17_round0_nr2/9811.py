#include <bits/stdc++.h>
using namespace std;

typedef long long unsigned llu;
typedef long long lld;
typedef long ld;

//Input and Output using files
#define gc 		getchar
#define pc 		putchar
#define RR 		freopen("input.txt", "r", stdin)
#define WR 		freopen("output.txt", "w", stdout)

//sortnames
#define ff 			first
#define ss 			second
#define clr 		clear()
#define pb 			push_back
#define pob 		pop_back
#define mp 			make_pair
#define gcd(a,b)    __gcd(a,b)
#define sz(a) 		((int)(a.size()))
#define len(a) 		((int)a.length())
#define all(vi) 	vi.begin(), vi.end()
#define IOS 		ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define SET(a,val)  memset(a,val,sizeof(a))

// Math Start
#define PI          acos(-1.0)
#define Pi          3.1415926535897932384626433832795
template<typename X> inline X square(const X& a) { return (a*a); }
template<typename X> inline X maxi(const X& a,const X& b) { return (a>b?a:b); }
template<typename X> inline X mini(const X& a,const X& b) { return (a>b?b:a); }

//fast input

int scan_d()		{bool minus = false;int result = 0;char ch;ch = gc();while (true){if (ch == '-') break;if (ch >= '0' && ch <= '9') break;ch = gc();}if (ch == '-') minus = true; else result = ch-'0'; while (true){ch = gc(); if (ch < '0' || ch > '9') break;result = (result<<3) + (result<<1) + (ch - '0');}if (minus) return -result; else return result;}
ld scan_ld()		{bool minus = false;ld result = 0;char ch;ch = gc();while (true){if (ch == '-') break;if (ch >= '0' && ch <= '9') break;ch = gc();}if (ch == '-') minus = true; else result = ch-'0'; while (true){ch = gc(); if (ch < '0' || ch > '9') break;result = (result<<3) + (result<<1) + (ch - '0');}if (minus) return -result; else return result;}
lld scan_lld()		{bool minus = false;lld result = 0;char ch;ch = gc();while (true){if (ch == '-') break;if (ch >= '0' && ch <= '9') break;ch = gc();}if (ch == '-') minus = true; else result = ch-'0'; while (true){ch = gc(); if (ch < '0' || ch > '9') break;result = (result<<3) + (result<<1) + (ch - '0');}if (minus) return -result; else return result;}
llu scan_llu()		{llu result = 0;char ch;ch = gc();while (true){if (ch == '-') break;if (ch >= '0' && ch <= '9') break;ch = gc();}result = ch-'0'; while (true){ch = gc(); if (ch < '0' || ch > '9') break;result = (result<<3) + (result<<1) + (ch - '0');}return result;}

//end of fast input

//fast output

//no line break
void print_d(int n)     	{if(n<0){n=-n;putchar('-');}int i=10;char output_buffer[10];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<10);}
void print_ld(ld n)     	{if(n<0){n=-n;putchar('-');}int i=11;char output_buffer[11];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<11);}
void print_lld(lld n)     	{if(n<0){n=-n;putchar('-');}int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<21);}
void print_llu(llu n)     	{int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<21);}

//new line
void println_d(int n)     	{if(n<0){n=-n;putchar('-');}int i=10;char output_buffer[11];output_buffer[10]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<11);}
void println_ld(ld n)     	{if(n<0){n=-n;putchar('-');}int i=11;char output_buffer[12];output_buffer[11]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<12);}
void println_lld(lld n)     {if(n<0){n=-n;putchar('-');}int i=21;char output_buffer[22];output_buffer[21]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<22);}
void println_llu(llu n)     {int i=21;char output_buffer[22];output_buffer[21]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<22);}

//special char
char sp;
void printsp_d(int n)     	{if(n<0){n=-n;putchar('-');}int i=10;char output_buffer[11];output_buffer[10]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<11);}
void printsp_ld(ld n)     	{if(n<0){n=-n;putchar('-');}int i=11;char output_buffer[12];output_buffer[11]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<12);}
void printsp_lld(lld n)     {if(n<0){n=-n;putchar('-');}int i=21;char output_buffer[22];output_buffer[21]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<22);}
void printsp_llu(llu n)     {int i=21;char output_buffer[22];output_buffer[21]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar(output_buffer[i]);}while(++i<22);}

//end of fast output

//constants
const lld MOD=1000000007;
#define INF 	1<<57
#define MAX 	1000001

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    int t,i,l,f,m,c,TT=1,sp;
    string s;
    cin>>t;
    while(t--)
    {
        f=1,m=0,sp=0;
        cin>>s;
        l=s.length();
        if(l==1)
        {
            cout<<"Case #"<<TT<<": "<<s<<"\n";
            TT++;
            continue;
        }
        else
        {
            while(f>0)
            {
                c=1,m=0;
                l=s.length();
                for(i=0;i<l-1;i++)
                {
                    if(m==1)
                        s[i+1]='9';
                    else
                    {
                        if(int(s[i]-'0')>int(s[i+1]-'0'))
                        {
                            if(s[i]!='1')
                                s[i]=s[i]-1;
                            else
                            {
                                s[i]=' ';
                                sp=1;
                            }
                            s[i+1]='9';
                            //i++;
                            m=1;
                        }
                        else
                            c++;
                    }
                }
                if(c==l)
                {
                    f=0;
                    break;
                }
            }
            if(sp==0)
                cout<<"Case #"<<TT<<": "<<s<<"\n";
            else
                cout<<"Case #"<<TT<<":"<<s<<"\n";
        }
        TT++;
    }
    return 0;
}

