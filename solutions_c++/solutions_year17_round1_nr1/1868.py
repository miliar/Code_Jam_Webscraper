#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int R, C;

int fill_left(char** cake, int i, int j, char c) {
  int n;
  for (n = j - 1; n >= 0; --n) {
    if (cake[i][n] == '?') {
      cake[i][n] = c;
    } else {
      break;
    }
  }

  return n + 1;
}

int fill_right(char** cake, int i, int j, char c) {
  int n;
  for (n = j + 1; n < C; ++n) {
    if (cake[i][n] == '?') {
      cake[i][n] = c;
    } else {
      break;
    }
  }

  return n - 1;
}

void fill_down(char** cake, int i, int left, int right, char c) {
  for (int n = i + 1; n < R; ++n) {
    bool allEmpty = true;
    for (int j = left; j <= right; ++j) {
      if (cake[n][j] != '?') {
        allEmpty = false;
        break;
      }
    }

    if (!allEmpty) {
      break;
    }

    for (int j = left; j <= right; ++j) {
      cake[n][j] = c;
    }
  }
}

void fill_up(char** cake, int i, int left, int right, char c) {
  for (int n = i - 1; n >= 0; --n) {
    bool allEmpty = true;
    for (int j = left; j <= right; ++j) {
      if (cake[n][j] != '?') {
        allEmpty = false;
        break;
      }
    }

    if (!allEmpty) {
      break;
    }

    for (int j = left; j <= right; ++j) {
      cake[n][j] = c;
    }
  }
}

char extend(char** cake, int i, int j) {
  char c = cake[i][j];
  int left = fill_left(cake, i, j, c);
  int right = fill_right(cake, i, j, c);
  fill_down(cake, i, left, right, c);
  fill_up(cake, i, left, right, c);
  return c;
}

int find_letter(char **cake, int i, bool* processed) {
  for (int j = 0; j < C; ++j) {
    char c = cake[i][j];
    if (c != '?' && !processed[c - 'A']) {
      return j;
    }
  }

  return -1;
}

void process_case() {
  cin >> R >> C;

  char **cake = new char*[R];
  bool *processed = new bool[26];
  for (int i = 0; i < R; ++i) {
    string line;
    cin >> line;
    cake[i] = new char[C];
    for (int j = 0; j < C; ++j) {
      cake[i][j] = line[j];
    }
  }

  memset(processed, 0, sizeof(bool) * 26);

  for (int i = 0; i < R; ++i) {
    while (true) {
      int letterIndex = find_letter(cake, i, processed);
      if (letterIndex == -1) {
        break;
      }

      char c = extend(cake, i, letterIndex);
      processed[c - 'A'] = true;
    }
  }

  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      cout << cake[i][j];
    }

    cout << endl;
  }

  for (int i = 0; i < R; ++i) {
    delete[] cake[i];
  }

  delete[] processed;
  delete[] cake;
}

int main() {
  int T;
  cin >> T;

  for (int n = 0; n < T; ++n) {
    cout << "Case #" << (n + 1) << ":" << endl;
    process_case();
  }
}
