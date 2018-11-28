#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

typedef struct heap {
  int size = 0;
  long *arr = NULL;
  int last = 0;

  void init(int s) {
    size = s;
    arr = (long *) malloc(sizeof(long) * size);
  }

  void resize(int s) {
    long *tmp = (long *) malloc(sizeof(long) * s);
    memcpy(tmp, arr, sizeof(long) * size);
    free(arr);
    size = s;
  }

  void destroy() {
    if (arr) {
      free(arr);
    }
    size = 0;
  }

  int parent(int index) {
    return (index - 1) / 2;
  }

  void bubble(int index) {
    if (arr[index] > arr[parent(index)]) {
      long tmp;
      tmp = arr[parent(index)];
      arr[parent(index)] = arr[index];
      arr[index] = tmp;
      bubble(arr[parent(index)]);
    }
  }
  
  void push(long l) {
    if (last == 0) {
      arr[0] = l;
      return;
    } 
    arr[last++] = l;
    bubble(last);
  }
} heap;

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    long n;
    long k;
    cin >> n >> k;
    int left_one = 0;
    long tmp = k;
    while (tmp) {
      tmp = tmp >> 1;
      left_one++;
    }
    long pieces = 1l << (left_one - 1);
    long piece_size = (n - (pieces - 1)) / pieces;
    long leftovers = (n - (pieces - 1)) % pieces;
    long piece;
    if (k - pieces < leftovers) {
      piece = piece_size + 1;
    } else {
      piece = piece_size;
    }
    cout << "Case #" << i + 1 << ": " << piece / 2 << " " << (piece & 1l ? piece / 2 : (piece / 2 - 1)) << endl;
  }
}
