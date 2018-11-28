#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

using namespace std;

char maximum_color(map<char,int> &m) {
    char result = 'R';
    if (m['Y'] > m[result]) result = 'Y';
    if (m['B'] > m[result]) result = 'B';
    return result;
}

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int N; cin >> N;
        map<char, int> colors;
        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V;
        colors['R'] = R;
        colors['Y'] = Y;
        colors['B'] = B;
        //cout << N << R << O << Y << G << B << V << endl;
        char answer[1000];
        for(int i = 0; i < N; i++) answer[i] = 0;
        answer[0] = maximum_color(colors);
        colors[maximum_color(colors)] -= 1;
        int impossible_flag = 0;
        int i = 2;
        while ((colors[answer[0]] > 0) && (i < N)) {
            answer[i] = answer[0];
            colors[answer[0]] -= 1;
            i += 2;
        }
        if (colors[answer[0]] > 0) impossible_flag = 1;
        else {
            i--;
            int med = i;
            //cout << "at " << i << endl;
            answer[med] = maximum_color(colors);
            colors[answer[med]] -= 1;
            i += 2;
            while ((colors[answer[med]] > 0) && (i < N)) {
                //cout << "->";
                answer[i] = answer[med];
                colors[answer[med]] -= 1;
                i += 2;
            }
            i = med - 2;
            while ((colors[answer[med]] > 0) && (i > 0)) {
                //cout << "->";
                answer[i] = answer[med];
                colors[answer[med]] -= 1;
                i -= 2;
            }
            if (colors[answer[med]] > 0) impossible_flag = 1;
        }
        if (impossible_flag == 0) {
            char last = maximum_color(colors);
            for (int i = 0; i < N; i++) {
                if (answer[i] == 0) answer[i] = last;
            }
        }
//            for (int k = 0; k < N; k++) printf("%c", answer[k]);
//            printf("\n");
            
        if (answer[N-1] == answer[0]) {
            impossible_flag = 1;
            //cout << "problem with round";
        }
        for (int i = 1; i < N; i++) if (answer[i] == answer[i-1]) {
            impossible_flag = 1;
            //cout << "problem with " << i;
            break;
        }
        if (impossible_flag == 1) printf("Case #%d: IMPOSSIBLE\n", t+1);
        else {
            printf("Case #%d: ", t+1);
            for (int i = 0; i < N; i++) printf("%c", answer[i]);
            printf("\n");
        }
    }
    return 0;
}
