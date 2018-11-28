#include <stdio.h>
#include <iostream>



using namespace std;

int main(int argc, char **argv)
{    
    
    int n; cin >> n;
    
    for (int i=0; i<n; ++i) {
        string s; cin >> s;
        int k; cin >> k;
        
        int f=0;
        
        for (int v=0; v <= s.length()-k; ++v) {
            if (s[v] == '-') {
                ++f;
                for (int t=0; t<k; ++t) {
                    s[v+t] = (s[v+t]=='-' ? '+' : '-');
                }
            }
            //cout << s << endl;
            //printf(">%d %d %s\n", v, f, s.c_str() );
        }
        
        bool r=true;
        
        for (int v=s.length()-k; v<s.length(); ++v) {
            //printf("%c", s[v]);
            if (s[v]=='-') {
                r = false;
            }
        }
        
        printf("Case #%d: ", i+1);
        if (r) {
            printf("%d\n", f);
        } else {
            printf("%s\n", "IMPOSSIBLE");
        }
        
    }
	
	return 0;
}
