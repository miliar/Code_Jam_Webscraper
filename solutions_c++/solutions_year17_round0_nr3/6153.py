#include<iostream>
#include<limits> //numeric_limits for stuff like numeric_limits<int>::max()
#include<iomanip> //iostream helper stuff like ignore, fixed, setprecision(int), setfill, setw (fieldwidth) get_money, get_time, setbase, setiosflags
//#include<algorithm>
#include<vector>
#include<cmath>
//#include<climits> //INT_MAX PI etc
#include<utility> //swap, make_pair, move, etc
#include<cstring>
#include<queue>
using namespace std;

/*************************template stuff*********************************/
typedef unsigned short us;
typedef long long ll;
typedef unsigned long long ull;

/*skip line in input*/
void skip_line() { cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); }

// Functor to compare by the Mth element of tuple
//template<int M, template<typename> class F = std::less>
//struct TupleCompare { template<typename T>
//    bool operator()(T const &t1, T const &t2) {
//        return F<typename tuple_element<M, T>::type>()(std::get<M>(t1), std::get<M>(t2));
//    }
//};
/*clamp value between low and high http://en.cppreference.com/w/cpp/algorithm/clamp*/template<class T, class Compare> constexpr const T& clamp( const T& v, const T& lo, const T& hi, Compare comp ) { return assert( !comp(hi, lo) ), comp(v, lo) ? lo : comp(hi, v) ? hi : v; }
/*print whole vec cout*/
template<typename T> void cout_print_vec(vector<T>& vec, ostream& os, string pre) {os<<pre<<" ";for(auto it:vec) os<<it<<" "; os<<"\n";}
/*print whole vec*/
template<typename T> void cerr_print_vec(vector<T>& vec, string pre) {cerr<<pre<<" ";for(auto it:vec) cerr<<it<<" "; cerr<<"\n";}
/*print array from a to b*/
template<typename T = int, const int K, typename B = int> void cerr_print_array(array<T, K>& array, B a=0, B b=K, string pre="ARRAY:") {cerr<<pre<<" ";for(auto i =a; i < b; i++) cerr<<array[i]<<" "; cerr<<"\n";}
/*vv print all args in macro call along with their names vv*/
#define cerrPrintAll(...) cerr<<"VARS: "; __printAll(#__VA_ARGS__, __VA_ARGS__)
/*http://stackoverflow.com/a/22965289/1102730*/ template <typename Arg1> void __printAll(const char* name, Arg1&& arg1) { std::cerr<<name<<"="<<arg1<<"\n"; } template <typename Arg1, typename... Args> void __printAll(const char* names, Arg1&& arg1, Args&&... args) { const char* comma = strchr(names + 1, ','); std::cerr.write(names, comma - names) << "=" << arg1; __printAll(comma, args...); }

/******************************end template stuff**************************************/
struct gap{
    //gap* lneighbor;
    //gap* rneighbor;
    long lPerson; long rPerson;
    long size;
    gap() {

    }
    gap(long lP, long rP) {
        lPerson= lP;
        rPerson= rP;
        size = rPerson - lPerson -1;
        //lneighbor= this; rneighbor=this;
    }

    gap(long lP, long rP, gap& other) {
        lPerson= lP;
        rPerson= rP;
        size = rPerson - lPerson -1;
        //lneighbor = other.lneighbor;
        //rneighbor = &other;
    }

    void updateSize() { size =rPerson - lPerson-1; }
};

gap splitGap(gap&a) {
    long lmid = (a.rPerson + a.lPerson)/2;
    //gap b (lmid, a.rPerson, a);
    gap b (lmid, a.rPerson);
    a.rPerson = lmid; a.updateSize();
    return b;
}

int main() {
    std::ios::sync_with_stdio(false);
	int t;
    long n, k;
    
    cin >> t;
    auto compare = [](gap& a, gap& b) { return a.size < b.size; };
    priority_queue<gap, deque<gap>, decltype(compare)> gap_queue(compare);
    for(int i=1; i <= t; ++i) {
        cin >> n >> k;
        if(n==k) {
            cout << "Case #" << i << ": 0 0\n";
            continue;
        }
        //gap lguard = {-1l, -1l};
        //gap rguard = {n, n};
        gap g = { -1l,n };
        //g.lneighbor = &lguard;
        //lguard.rneighbor = &g;
        //rguard.lneighbor = &g;
        //g.rneighbor = &rguard;
        gap_queue.push(g);

        //cerr << "working" << endl;
        gap topgap; gap othergap;
        for(int i= 0; i < k; ++i) {
            topgap = gap_queue.top(); gap_queue.pop();
            //cerrPrintAll(topgap.lPerson, topgap.rPerson, topgap.size);
            othergap = splitGap(topgap);
            //cerrPrintAll("after split: ", topgap.lPerson, topgap.rPerson, topgap.size);
            //cerrPrintAll(othergap.lPerson, othergap.rPerson, othergap.size);
            gap_queue.push(topgap);
            gap_queue.push(othergap);
        }
        //cerr << "done working" << endl;

        while(!gap_queue.empty()) {
            gap t = gap_queue.top(); gap_queue.pop();
            //cerrPrintAll(t.lPerson, t.rPerson, t.size);
        }

        long lsize, ssize;
        lsize=topgap.size; ssize=othergap.size;
        if(lsize<ssize) { swap(lsize, ssize); }

        cout << "Case #" << i << ": " << lsize << " "  << ssize << "\n";
    }
    return 0;    
}
