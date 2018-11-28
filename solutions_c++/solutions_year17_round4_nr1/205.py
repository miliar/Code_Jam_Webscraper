
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;


ll solve2(std::vector<int>& mod)
{
    std::cerr << "Initial mod is";
    for ( int i = 0 ; i < mod.size() ; ++i )
        std::cerr << ' ' << mod[i];
    std::cerr << std::endl;

    int P = mod.size();
    // output is "# of sets adding up to 0 mod P" + 1?
    int out = 1;
    out += mod[0];
    mod[0] = 0;

    // 1+1
    {
        int a = mod[1] / 2;
        out += a;
        mod[1] -= 2*a;
    }

    int leftInMod = 0;
    for ( int i = 0 ; i < P ; ++i )
        leftInMod += mod[i];
    if ( leftInMod == 0 )
        return out-1;
    else
        return out;

    std::cerr << "mod is";
    for ( int i = 0 ; i < mod.size() ; ++i )
        std::cerr << ' ' << mod[i];
    std::cerr << std::endl;
}

ll solve3(std::vector<int>& mod)
{
    int P = mod.size();
    // output is "# of sets adding up to 0 mod P" + 1?
    int out = 1;
    out += mod[0];
    mod[0] = 0;

    // 1 + 2
    {
        int a = std::min( mod[1] , mod[2] );
        out += a;
        mod[1] -= a;
        mod[2] -= a;
    }
    // 1+1+1
    {
        int b = mod[1] / 3;
        out += b;
        mod[1] -= 3*b;
    }
    // 2+2+2
    {
        int c = mod[2] / 3;
        out += c;
        mod[2] -= 3*c;
    }

    int leftInMod = 0;
    for ( int i = 0 ; i < P ; ++i )
        leftInMod += mod[i];
    if ( leftInMod == 0 )
        return out-1;
    else
        return out;

    std::cerr << "mod is";
    for ( int i = 0 ; i < mod.size() ; ++i )
        std::cerr << ' ' << mod[i];
    std::cerr << std::endl;
}

ll solve4(std::vector<int>& mod)
{
    int P = mod.size();
    // output is "# of sets adding up to 0 mod P" + 1?
    int out = 1;
    out += mod[0];
    mod[0] = 0;

    // 3 + 1
    {
        int a = std::min( mod[3] , mod[1] );
        out += a;
        mod[3] -= a;
        mod[1] -= a;
    }
    // 2 + 2
    {
        int b = mod[2] / 2;
        out += b;
        mod[2] -= 2*b;
    }
    // 2+1+1
    {
        int c = std::min( mod[2] , mod[1]/2 );
        out += c;
        mod[2] -= c;
        mod[1] -= 2*c;
    }
    // 2+3+3
    {
        int d = std::min( mod[2] , mod[3]/2 );
        out += d;
        mod[2] -= d;
        mod[3] -= 2*d;
    }
    // 1+1+1+1
    {
        int e = mod[1] / 4;
        out += e;
        mod[1] -= 4*e;
    }
    // 3+3+3+3
    {
        int f = mod[3] / 4;
        out += f;
        mod[3] -= 4*f;
    }

    int leftInMod = 0;
    for ( int i = 0 ; i < P ; ++i )
        leftInMod += mod[i];
    if ( leftInMod == 0 )
        return out-1;
    else
        return out;

    std::cerr << "mod is";
    for ( int i = 0 ; i < mod.size() ; ++i )
        std::cerr << ' ' << mod[i];
    std::cerr << std::endl;
}

ll solve()
{
    int N;
    int P;
    std::cin >> N >> P;
    std::vector<int> dat( N );
    for ( int i = 0 ; i < N ; ++i )
        std::cin >> dat[i];

    std::vector<int> mod( P );
    for ( int i = 0 ; i < N ; ++i )
        ++mod[ dat[i]%P ];

    switch ( P ) {
        case 2:
            return solve2( mod );
        case 3:
            return solve3( mod );
        case 4:
            return solve4( mod );
        default:
            return -1;
    }
}

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {

        std::cout << "Case #" << testID << ": ";
        
        ll result = solve();

        std::cout << result << "\n";
    }

    return 0;
}
