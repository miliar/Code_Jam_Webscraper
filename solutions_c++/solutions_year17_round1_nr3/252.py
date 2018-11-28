
#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

typedef long long ll;

ll c(ll a, ll b)
{
    return (a-1) / b + 1;
}

ll aturns(ll H2, ll A1, ll B, ll b)
{
    return (H2 - 1) / (A1 + b*B) + 1 + b;

    ll denom = A1 + b*B;
    ll out = H2 / denom + 1;
    if ( H2 % denom == 0 )
        --out;

    out += b;
    return out;
}

ll costnow(int H1, int h1, int a2, int aturns) {
//    std::cerr << "in costnow. H1 = " << H1 << " h1 = " << h1 << " a2 = " << a2 << " aturns = " << aturns << std::endl;
    // fight until we need to heal.
    int cost = 0;
    while ( true ) {
        // can we safely attack?
        if ( h1 > a2 && aturns > 1 ) {
            ++cost;
            --aturns;
            h1 -= a2;
        } else if ( aturns == 1 ) { // can we desperately attack?
//            std::cerr << "Result: " << cost+1 << std::endl;
            return cost + 1;
        } else
            break;
    }

    // ok, next turn is spent healing.
    int denom = c( H1 , a2 ) - 2;
    if ( denom <= 0 )
        return -1;
    int cures = c( aturns-1 , denom );
//    std::cerr << "aturns " << aturns << " attacks per cure: " << denom << " cures " << cures << " returning " << cost+cures << std::endl;

    return cost + cures + aturns;
}

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {
        
        ll H1;
        ll A1;
        ll H2;
        ll A2;
        ll B;
        ll D;

        std::cin >> H1 >> A1;
        std::cin >> H2 >> A2;
        std::cin >> B  >> D ;

        // Can I win in one turn?
        if ( A1 >= H2 ) {
            std::cout << "Case #" << testID << ": 1\n";
            continue;
        }

        // How many attacking turns are needed?
//        ll minA = 0; // definitely too small.
//        ll maxA = 2e9; // definitely large enough.
//        while ( 
        int bestB = -1;
        int bestAturns = 2e9;
        for ( int b = 0 ; b <= 100 ; ++b ) {
            int aturnsCurr = aturns( H2 , A1 , B , b );
            if ( aturnsCurr < bestAturns ) {
                bestB = b;
                bestAturns = aturnsCurr;
            }
        }

        std::cerr << "bestAturns: " << bestAturns << std::endl;

        // how many defending turns are needed to buy me this much time?
        int bestD = -1;
        int bestResult = 2e9;
        int h1 = H1;
        int a2 = A2;
        int currDturns = 0;
        for ( int d = 0 ; d <= 250 ; ++d ) {
            // what happens if I just fight it out right now?
            int currResult = costnow( H1 , h1 , a2 , bestAturns );
            std::cerr << "d = " << d << " currResult = " << currResult << std::endl;
            if ( currResult >= 0 && currResult + currDturns < bestResult )
                bestResult = currResult + currDturns;

            if ( D == 0 ) {
                // no point defending. Just take whatever we got by fighting directly.
                break;
            }
            
            ++currDturns;
            // can I defend this turn?
            if ( h1 > a2 - D ) {
                a2 -= D;
                if ( a2 <= 0 ) {
                    // dturns = currDturns is a valid method.
                    if ( currDturns + bestAturns < bestResult )
                        bestResult = currDturns + bestAturns;
                    break;
                }
                h1 -= a2;
            } else {
                // guess I have to cure instead.
                int newh1 = H1 - a2;
                if ( newh1 <= h1 ) {
                    // we're just gonna have to cure again next turn.
                    // can't win the fight!
                    assert( bestResult >= 1.5e9 );
                    break;
                } else {
                    h1 = newh1;
                }
            }
        }

        if ( bestResult > 1.5e9 )
            std::cout << "Case #" << testID << ": IMPOSSIBLE\n";
        else
            std::cout << "Case #" << testID << ": " << bestResult << '\n';
        
    }
    return 0;
}
