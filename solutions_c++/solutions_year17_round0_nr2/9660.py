/* Copyright (c) 2015 Martin Váňa */

/* http://www.cplusplus.com/reference/ */
#include <bits/stdc++.h>
using namespace std;

// Debug printing
#ifdef DEBUG
#define DBG(args...)                printf("DBG> ");printf(args);
#else
#define DBG(args...)                // Just strip off all debug tokens
#endif

// Printing
#define PR(args...)                 printf(args)

// Useful constants
#define STR_BUF                     1001
#define INF                         1000000000   // avoid overflow while addding
#define EPS                         1e-9
#define PI                          3.1415926535897932384626433832795//atan(1)*4

// Input macros
#define S(n)                        scanf("%d",&n)
#define SC(n)                       scanf("%c",&n)
#define SL(n)                       scanf("%lld",&n)
#define SF(n)                       scanf("%lf",&n)
#define SS(n)                       scanf("%s",n)

// For loops
#define F(i,L,U)                    for((i)=(L);(i)<(U);(i)++)
#define FE(i,L,U)                   for((i)=(L);(i)<=(U);(i)++)
#define RF(i,L,U)                   for((i)=(U);(i)>(L);(i)--)
#define RFE(i,L,U)                  for((i)=(U);(i)>=(L);(i)--)

// Checking bounds
#define IN(i,l,r)                   ((l)<(i)&&(i)<(r))
#define LINR(i,l,r)                 ((l)<=(i)&&(i)<=(r))
#define LIN(i,l,r)                  ((l)<=(i)&&(i)<(r))
#define INR(i,l,r)                  ((l)<(i)&&(i)<=(r))

// Bit operations
#define OR(a,b)                     ((a)|(b))
#define AND(a,b)                    ((a)&(b))
#define XOR(a,b)                    ((a)^(b))
#define BIT(x,i)                    ((x)&(1<<(i)))       //select the bit of position i of x
#define LBIT(x)                     ((x)&((x)^((x)-1)))  //get the lowest bit of x
// CP3 Bit operations
#define IS_ON(S, j)                 (S & (1 << j))
#define SET_BIT(S, j)               (S |= (1 << j))
#define CLEAR_BIT(S, j)             (S &= ~(1 << j))
#define TOOGLE_BIT(S, j)            (S ^= (1 << j))
#define LOW_BIT(S)                  (S & (-S))
#define SET_ALL(S, n)               (S = (1 << n) - 1)
// CP3 Bit operations
#define MODULO(S, N)                ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define IS_POWER_OF_TWO(S)          (!(S & (S - 1)))
#define NEAREST_POWER_OF_TWO(S)     ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define TURN_OFF_LAST_BIT(S)        ((S) & (S - 1))
#define TURN_ON_LAST_ZERO(S)        ((S) | (S + 1))
#define TURN_OFF_LAST_CONSECUTIVE_BITS(S)    ((S) & (S + 1))
#define TURN_ON_LAST_CONSECUTIVE_ZEROES(S)   ((S) | (S - 1))

// Some common useful functions
#define SIGN(x)                     ((x)>0)-((x)<0)
#define ABS(x)                      ((x)<0?(-(x)):(x))
#define MIN(a,b)                    (((a)<(b))?(a):(b))
#define MAX(a,b)                    (((a)>(b))?(a):(b))
#define REMAX(a,b)                  (a)=MAX((a),(b))      // set a to the maximum of a and b
#define REMIN(a,b)                  (a)=MIN((a),(b));
#define CB(n,b)                     (((n)>>(b))&1)
#define C2I(c)                      (c-'0')               // char to int
#define DIGITS(i)                   (int)((log(i)/log(10))+1)
#define DROUND(num)                 (int)floor((num)+0.5) // Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define IS_ODD(n)                   ((n)%2!=0)

// Variable definitions
#define DI(n)                       int n
#define DD(n)                       double n
#define DS(s,N)                     char s[N]
#define DIS(n)                      DI(n);S(n)

// Contest
#define TESTS                       DIS(_tc_no_);while(_tc_no_--)
#define CASES                       int _c_no_,_case_;S(_c_no_);FE(_case_,1,_c_no_)
#define LINE(line)                  fgets(line,sizeof(line),stdin)
#define LINE_BY_LINE(line)          while(LINE(line))
#define DEF_SEP_LINE                DI(_fline_);_fline_=1;   // separate test cases with blank line
#define SEP_LINE                    (_fline_==1)?_fline_=0:PR("\n");

// Arrays
#define CLR(a)                      memset(a,0,sizeof(a))  // set elements of array to zeroes
#define MS(a, v)                    memset(a,v,sizeof a)  // fills memory with value v (only for 0 or -1)
#define SET(a,c,v)                  fill(a,a+c,v)  // set elements of array to some value
#define PRAI(i,a,L,R)               F(i,L,R){PR("%3d ",a[i]);}PR("\n")
#define PRAF(i,a,L,R)               F(i,L,R){PR("%lf ",a[i]);}PR("\n")
#define PRAS(i,a,L,R)               F(i,L,R){PR("%s ",a[i]);}PR("\n")

// Colections
#define FOREACH(v,c)                for(auto v = (c).begin();  v != (c).end(); ++v)
#define ALL(c)                      (c).begin(), (c).end()
#define PB                          push_back
#define PF                          push_front
#define MP                          make_pair
#define SZ(a)                       ((int)(a.size()))

// Directions
const int D4[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int D6[6][3] = {{0,1,0}, {0,-1,0}, {1,0,0}, {-1,0,0}, {0,0,1}, {0,0,-1}};
const int D8[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};

// Data types
typedef long long          LL;
typedef unsigned long long ULL;
typedef unsigned int       UI;
typedef unsigned short     US;
typedef pair<int, int>     II;
typedef pair<int, double>  IF;
typedef pair<double, int>  FI;
typedef vector<II>         VII;
typedef vector<IF>         VIF;
typedef vector<FI>         VFI;
typedef vector<int>        VI;
typedef vector<double>     VF;
typedef vector<bool>       VB;

// Problem complex structures and algorithms

// Problem specific data

////////////////////////////////////////////////////////////////////////////////
//                                                                            //
////////////////////////////////////////////////////////////////////////////////

#define SOME_MAGIC_CONSTANT 666

int t;
char line[STR_BUF];
char *result;

int main() {
    int z, i, j, k, l, len;

    // read number of lines
    SS(line);
    t = atoi(line);

    FE(z,1,t){
        // read line
        SS(line);
        result = line;
        len = (int) strlen(line);
        // PR("len %d\n", len);

        // select first char
        char curr_char = line[0];

        // for other chars
        F(j,1,len) {
            if (curr_char <= line[j]) {
                // if is tidy number
                // continue
                curr_char = line[j];
                continue;
            }

            // if is not tidy number
            // move back from first occurence of broken tidy sequence
            RFE(k,0, j-1) {
                // decrement previous character
                line[k]--;
                if (k == 0) {
                    // we fixed the number
                    // set all chars on the right to '9'
                    F(l,k+1, len) {
                        line[l] = '9';
                    }

                    if (line[k] == '0') {
                        result++;
                    }
                    break;
                } else {
                    if (line[k-1] <= line[k]){
                        // we fixed the number
                        // set all chars on the right to '9'
                        F(l,k+1, len) {
                            line[l] = '9';
                        }
                        break;
                    }
                }
            }
            break;
        }

        PR("Case #%d: %s\n", z, result);
    }

    exit( EXIT_SUCCESS );
}
