#include <cstdio>
#include <vector>
using namespace std;

std::vector<char> cakes;

void flip(int from, int n) {
    for (int i = from; i < from+n; i++) {
        cakes[i] = cakes[i] == '+' ? '-' : '+';
    }
}

void c(int num, int size) {
    int flips = 0;
    for (int i = 0; i < cakes.size(); i++) {
        if (cakes[i] == '-') {
            if ((cakes.size() - i) < size) break;
            flips++;
            flip(i, size);
        }
    }
    bool ok = true;
    for (int i = 0; i < cakes.size(); i++) {
        if (cakes[i] == '-') {
            ok = false;
            break;
        }
    }
    printf("Case #%d: ", num+1);
    if (ok) {
        printf("%d\n", flips);
    } else {
        printf("IMPOSSIBLE\n");
    }
}

int main() {
    int cases;
    scanf("%d\n", &cases);

    for (int i = 0; i < cases; i++) {
        cakes.clear();
        while (true) {
            char ch = getchar();
            if (ch != '+' && ch != '-') {
                break;
            }
            cakes.push_back(ch);
        }
        int size;
        scanf("%d\n", &size);
        c(i, size);
    }
}
