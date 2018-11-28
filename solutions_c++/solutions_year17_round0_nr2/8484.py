#include <iostream>
#include <string>

using namespace std;

void makeTidyNumber ( string &num, int i ) {
    if ( i >= num.length() - 1 )
        return;
    
    if ( num [ i ] > num [ i + 1 ] ) {
        num [ i ]--;
        
        for ( int j = i + 1; j < num.length(); ++j )
            num [ j ] = '9';
    }
}

int main()
{
    freopen("/Users/kuk/Documents/studio/GCJ/GCJ/in.txt", "r", stdin);
    freopen("/Users/kuk/Documents/studio/GCJ/GCJ/out.txt", "w", stdout);
    
    int T; cin >> T;
    
    
    int caseNo = 0;
    while ( T-- > 0 ) {
        caseNo++;
        string givenNum; cin >> givenNum;
        string result = givenNum;
        for ( int i = (int)givenNum.length() - 1; i > -1; --i )
            makeTidyNumber( result, i );
        
        int notLeadingZeroIndex = 0;
        for ( int i = 0; i < (int)result.length(); i++ )
            if ( result [ i ] != '0' ) {
                notLeadingZeroIndex = i;
                break;
            }
        
        printf("Case #%d: ", caseNo);
        for ( int i = notLeadingZeroIndex; i < (int)result.length(); ++i )
            printf("%c", result[i]);
        printf("\n");
    }
    return 0;
}
