#include <vector>
#include <functional>
#include <map>
#include <array>
#include <utility>
#include <iterator>
#include <cstdio>
template<typename T> struct ScanfSpecifier{};
#define DEF(T,V) template<> struct ScanfSpecifier<T>{static constexpr const char* value = V;};
DEF(char*,"%s")DEF(int,"%d")DEF(double,"%lf")DEF(float,"%f")DEF(char,"%c")DEF(const char*,"%s")DEF(unsigned long,"%lu")DEF(unsigned int, "%u")
#ifdef _MSC_VER
DEF(long long int,"%I64d")
#else
DEF(long long int,"%lld")
#endif
#undef DEF
template<typename T> int RD(T& arg){return std::scanf(ScanfSpecifier<T>::value, &arg);}
template<int S> int RD(char (&arg)[S]){return std::scanf("%s", arg);}
int RD(char* arg){return std::scanf("%s", arg);}
template<> int RD<char>(char& arg){return std::scanf(" %c", &arg);}
template<typename T, typename... Args> int RD(T& arg1, Args&... args) {return RD(arg1) + RD(args...);}
template<typename T> T RD(){T ret; RD(ret); return ret;}
template<typename It> void RDV(It begin, It end) { while(begin != end) RD(*begin++); }
template<typename C> void RDV(C& c) {RDV(std::begin(c), std::end(c));}
template<typename T> void WT(T arg) {std::printf(ScanfSpecifier<T>::value, arg); }
template<typename T, typename U> void WT(std::pair<T, U> arg) {std::printf("("); WT(arg.first); std::printf(", "); WT(arg.second); std::printf(")");}
template<typename... Args> void WT(Args... args) { int alc = 0; int dummy[] = {((alc++? std::printf(" "): 0), WT(args), 0)...}; }

template<typename... Args> void WTL(Args... args) { WT(args...); std::printf("\n"); }
template<typename It> void WTV(It begin, It end) { int alc = 0; while(begin != end) (alc++? std::printf(" "): 0), WT(*begin++); }
template<typename C> void WTV(const C& c) {WTV(std::begin(c), std::end(c));}
template<typename It> void WTVL(It begin, It end) { WTV(begin, end); std::printf("\n"); }
template<typename C> void WTVL(const C& c) {WTVL(std::begin(c), std::end(c));}

#define _M_VARGS_NUM_IMPL(_1, _2, _3, _4, _5, _6, N, ...) N
#define _M_VARGS_NUM(...) _M_VARGS_NUM_IMPL(__VA_ARGS__, 6, 5, 4, 3, 2, 1)
#define _W1(_1) (#_1[0] == '"' || #_1[0] == '\''? WT("", _1, ""): WT('[', #_1, '=', _1, ']'))
#define _W2(_1, _2) (_W1(_1), _W1(_2))
#define _W3(_1, _2, _3) (_W1(_1), _W2(_2, _3))
#define _W4(_1, _2, _3, _4) (_W1(_1), _W3(_2, _3, _4))
#define _W5(_1, _2, _3, _4, _5) (_W1(_1), _W4(_2, _3, _4, _5))
#define _WW_IMPL2(num, ...) _W ## num(__VA_ARGS__)
#define _WW_IMPL(num, ...) _WW_IMPL2(num, __VA_ARGS__)
#define WW(...) (std::printf("(%03d) ", __LINE__), _WW_IMPL(_M_VARGS_NUM(__VA_ARGS__), __VA_ARGS__), WTL(""))




struct Range
{   
    struct It {   int num, step; int operator*(){return num;} void operator++(){num += step;} bool operator!=(const It& other){return num != other.num;} };
    Range(int ee):b(0),e(ee){}
    Range(int bb, int ee):b(bb), e(ee){}
    It begin(){return {b, (b < e? 1: -1)};}
    It end(){return {e, 0};}
    int b, e;
};

template<typename T> inline T& UMAX(T& x, T y){if(x < y)x = y; return x;}
template<typename T> inline T& UMIN(T& x, T y){if(y < x)x = y; return x;}
template<typename T, typename... Args> struct ArithmiticPromotion { typedef decltype(T() + typename ArithmiticPromotion<Args...>::type()) type; };
template<typename T, typename U> struct ArithmiticPromotion<T, U> { typedef decltype(T() + U()) type; };
template<typename T> struct ArithmiticPromotion<T, T> { typedef T type; };
template<typename T> struct ArithmiticPromotion<T> { typedef T type; };
template<typename T, typename U> typename ArithmiticPromotion<T, U>::type MAX(T a, U b) { return a < b? b: a; }
template<typename T, typename... Args> typename ArithmiticPromotion<T, Args...>::type MAX(T a, Args... args) { return MAX(a, MAX(args...)); }
template<typename T, typename U> typename ArithmiticPromotion<T, U>::type MIN(T a, U b) { return a < b? a: b; }
template<typename T, typename... Args> typename ArithmiticPromotion<T, Args...>::type MIN(T a, Args... args) { return MIN(a, MIN(args...)); }





//alias
//RD[L],RDV[L],WT[L],WTV[L] for i/o
using RG = Range;
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstring>
using namespace std;

void solve()
{
    int N, P;
    RD(N, P);


    int R[64];
    RDV(R, R + N);

    vector<pair<int, int>> seg[64];
    bool pass[64][64] = {};

    for(int i: RG(N))
    {
        for(int j: RG(P))
        {
            int q;
            RD(q);

            int l = (q * 100 + R[i] * 110 - 1) / (R[i] * 110);
            int r = q * 100 / (R[i] * 90);

            if(l <= r)
                seg[i].push_back({l, r});
        }

        sort(seg[i].begin(), seg[i].end(), [](auto a, auto b){return a.second < b.second;});
    }

    int ans = 0;
    for(auto s: seg[0])
    {
        vector<int> idx(N, -1);
        bool check = true;
        for(int i: RG(1, N))
        {
            for(int j: RG(seg[i].size()))
                if(!pass[i][j])
                    if(max(seg[i][j].first, s.first) <= min(seg[i][j].second, s.second))
                        if(idx[i] == -1 || seg[i][idx[i]].second > seg[i][j].second)
                            idx[i] = j;

            if(idx[i] == -1)
                check = false;
        }
        if(!check)
            continue;

        for(int i: RG(1, N))
            pass[i][idx[i]] = true;
        ans++;

    }

    WTL(ans);
}

int main()
{
    int T;
    RD(T);
    for(int tn: Range(1, T + 1))
    {
        printf("Case #%d: ", tn);
        solve();
    }
}




