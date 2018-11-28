//                                                  In The Name Of God
//                                              programmer:Mohammad Dehghan
#include <iostream>
using namespace std;

#include <vector>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <map>
#include <iomanip>
#include <queue>
#include <algorithm>
#include <sstream>

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef pair<long double, long double> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef vector<vvii> vvvii;
typedef vector<vector<viii>> vvviii;
typedef vector<vector<iii>> vviii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;
typedef vector<dd> vdd;

//#define inf 1000000000
//#define eps 1e-9


//int main() {
//    ios::sync_with_stdio(0);
//    int tc; cin >> tc;
//    for(int i = 1; i <= tc; i++) {
//        ll d, n = 0; cin >> d >> n;
//        double t = 0;
//        for(int i = 0; i < n; i++) {
//            ll dd, s; cin >> dd >> s;
//            t = max(t, (double)(d - dd) / s);
//        }
//        cout << "Case #" << i << ": ";
//        cout << fixed << setprecision(6) << d / t << endl;
//
//    }
//
//
//    return 0;
//}

vii horses;

int main() {

    long int tc;
    cin >> tc;
    int number = 0;
    while (tc--) {
        long long D, N;
        cin >> D >> N;
        number++;
        horses.clear();
        horses.resize(N);
        for (long int i = 0; i < N; ++i) {
            cin >> horses[i].first >> horses[i].second;
        }
        long double ti = 0;
        for (int j = 0; j < N; ++j) {
            if (ti < (D - horses[j].first) / horses[j].second)
                ti = (D - horses[j].first) / horses[j].second;
        }
        cout << "Case #" << number << ": " << setprecision(6) << std::fixed << (D / ti) << endl;
    }
}
//        if(N == 1){
//            long double ti = (D - horses[0].first)/horses[0].second;
//            cout <<"Case #"<<number<<": "<<setprecision(6) <<std::fixed<< (D/ti)<<endl;
//        }
//        else if(N==2){
//            long double ti = max( (D - horses[0].first)/horses[0].second ,(D - horses[1].first)/horses[1].second );
//            cout <<"Case #"<<number<<": " <<setprecision(6)<<std::fixed <<(D/ti)<<endl;
//        }



//int n , m;
//viii domines;
//vii finallist;
//ii first , last;
//bool finished = false;
//
//void backtrack (int index) {
//    if (index == n + 1) {
//        finished = true;
//        return;
//    }
//    for (int i = 0; i < 2*m && !finished; ++i) {
//        if (!domines[i].first && (domines[i].second.first == finallist[index - 1].second)) {
//            if (index == n && (domines[i].second.second != last.first))
//                continue;
//            finallist[index] = domines[i].second;
//            domines[i].first = 1;
//            if (!(i % 2))
//                domines[i + 1].first = 1;
//            else
//                domines[i - 1].first = 1;
//            backtrack(index + 1);
//            domines[i].first = 0;
// //           domines[i].second = make_pair(inf , inf);
//            if (!(i % 2)) {
//                domines[i + 1].first = 0;
// //               domines[i + 1].second = make_pair(inf, inf);
//            }
//            else {
//                domines[i - 1].first = 0;
//  //              domines[i - 1].second = make_pair(inf, inf);
//            }
//        }
//    }
//
//}
//
//int main(){
//
//    while (cin >> n >> m && n){
//        domines.clear();
//        domines.resize(2*m,make_pair(0 , make_pair(0,0)));
//        finallist.clear();
//        finallist.resize(n+1);
////        finallist[n-1].first = last.first;
////        finallist[n-1].second = last.second;
//        cin>>first.first>>first.second>>last.first>>last.second;
//        finallist[0].first = first.first;
//        finallist[0].second = first.second;
//        for (int i = 0; i < 2*m; ++i) {
//            cin>>domines[i].second.first>>domines[i].second.second;
//            domines[i+1].second.first = domines[i].second.second;
//            domines[i+1].second.second = domines[i].second.first;
//            ++i;
//        }
//        backtrack(1);
//        if(finished)
//            cout <<"YES"<<endl;
//        else
//            cout << "NO"<<endl;
//        finished = false;
//    }
//}

//
//int main(){
//
//    int tc ;
//    cin >> tc;
//    while (tc--){
//        int n ;
//        cin >> n;
//        int min =2 ;
//        int i , n2 = (n-4)/2;
//        for ( i = 1; i <=2*n2; ++i) {
//            min+=i*2;
//        }
//        if((n-4) % 2 == 1)
//            min+= i;
//        cout << min<<endl;
//    }
//
//}


//99
//2525 1
//2400 5
//300 2
//120 60
//60 90
//2 1
//1 10000
//131077822 1
//105930950 3608
//951474064 1
//605617783 1854
//932241924 1
//250413260 5563
//251976750 1
//37523298 6912
//99152721 1
//58354860 1926
//783018707 1
//88121307 4131
//639338367 1
//291203113 6378
//672514796 1
//170175618 8738
//287774565 1
//190526946 9796
//38994305 1
//10780080 6841
//1000000000 1
//999999999 1
//285136113 1
//112216518 9297
//273333115 1
//199748352 7776
//241712373 1
//233348860 4651
//1000000000 2
//100 10000
//200 10000
//652009174 1
//338724449 352
//352537441 1
//208600649 3594
//1000000000 2
//999999996 3
//999999997 2
//402968800 1
//146355729 3814
//900178370 1
//691948054 3451
//123392396 1
//62644635 2299
//609693185 1
//482964044 9690
//289799855 1
//119110900 10000
//613708385 1
//207593466 436
//10624065 1
//7660000 5131
//319827779 1
//233417751 5372
//704981430 1
//434585122 6050
//557998694 1
//385991442 4632
//238116277 1
//124154500 3903
//599586097 1
//168139845 2005
//2 1
//1 1
//372391542 1
//359873480 177
//413918839 1
//254928106 1093
//842764022 1
//658957576 4070
//784534362 1
//268746719 8114
//205951222 1
//114775068 901
//306794940 1
//304497843 1344
//1000000000 2
//2 2
//1 3
//694325937 2
//34215164 1166
//582636968 9692
//472533887 1
//108306906 1794
//1000000000 2
//999999998 3
//999999999 2
//726480404 1
//327840527 9277
//475150098 1
//407953706 4021
//1000000000 2
//12345675 3
//12345676 2
//388370869 1
//381026582 410
//585584419 1
//525156031 4916
//392533744 1
//147506468 7033
//601128505 1
//41357453 5135
//739344631 1
//432447251 7431
//899094944 1
//644586485 1113
//541000239 1
//138218162 4140
//334146606 2
//105422380 7667
//285743300 2394
//524065206 1
//145094512 4290
//690438607 1
//417609260 8697
//634155725 1
//369081537 64
//71029611 1
//63620453 8392
//788982628 1
//764761697 1715
//1000000000 2
//999000000 10000
//998000000 10000
//586330136 1
//416104919 7260
//974323101 1
//364680900 2441
//140899898 1
//5967101 9667
//527347037 1
//83937058 6980
//1000000000 1
//1 1
//838241117 1
//369982007 1821
//204099020 1
//146539679 7474
//756005869 1
//733105085 9319
//905751325 1
//617152714 8229
//386505314 1
//108917676 801
//121872146 1
//111514347 6707
//885278578 1
//113187929 9117
//17305691 1
//5104584 7370
//279273193 1
//269999131 5890
//715117710 1
//530291656 6727
//750837609 1
//392277806 5209
//243133077 1
//188915973 6229
//96964909 1
//86353596 7617
//538785005 1
//171300038 4040
//1000000000 2
//998000000 1
//999000000 1
//1000000000 1
//1 10000
//581217043 1
//61393681 2377
//395351612 1
//124892568 8238
//731299822 1
//44667286 1729
//200000 2
//5001 1
//5000 6
//230520328 1
//210198390 1254
//717440572 1
//240408593 7958
//741024937 1
//519308978 8851
//646254995 1
//330233771 3441
//163010463 1
//98094045 1777
//472730072 1
//352244381 2127
//1000000000 2
//999999997 3
//999999998 2
//199204510 1
//36606297 2361
//747306642 1
//547707522 3524
//315995728 1
//214982115 1703
//563697987 1
//200471299 1186
//1000000000 1
//999999999 10000
//636835443 1
//329016383 7064
