import java.util.*;
public class tictactoe {
    public static String[][] board = Collections.nCopies(3, Collections.nCopies(3, "- ").toArray(new String[0])).toArray(new String[0][0]);
    public static void main(String[] args) {
        System.out.println(Arrays.deepToString(board).replaceAll("], ","\n").replaceAll("[\\]\\[,]",""));
    }
}